import re
from summa import summarizer, keywords

import pymorphy2
from razdel import sentenize, tokenize
from navec import Navec
from slovnet import Morph

from .drawing_presets import preset_barplot, preset_pie, preset_plot
import os

### --------------------- SUMMARIZATION --------------------- ###
def clean_text(texts):
    pattern = r"[А-Яа-яЁё0-9](\.)(?!\d)"
    return re.sub(pattern, lambda x: x.group().replace(".", ""), texts)
    

def process_text(texts):
    texts = clean_text(texts)
    summarized_sentences = summarizer.summarize(texts, language='russian', split=True)
    return summarized_sentences


def get_keywords(summarized_sentences, morph_analyzer):
    kw = keywords.keywords("".join(summarized_sentences), language='russian', split=True)
    keywords_set = set()
    for w in kw:
        proc_word = morph_analyzer.parse(w)[0].normal_form
        if len(proc_word) <= 2 or ' ' in proc_word:
            continue
        keywords_set.add(proc_word)
    return keywords_set

### --------------------- NUMERIC ENTITIES EXTRACTION --------------------- ###
class NumericEntity(object):
    def __init__(self, number):
        self.number = number
        self.pct = False
        
        self.entity = None
        self.normal_form = None
        
    def update_entity(self, entity, normal_form):
        self.entity = entity
        self.normal_form = normal_form
    
    def __str__(self):
        return f"NumericEntity(number={self.number}, entity={self.entity}, normal_form={self.normal_form}, percent={self.pct})"
    

def extract_numeric_entities(text, morph, morph_analyzer):
    chunk = []
    for sent in sentenize(text):
        tokens = [_.text for _ in tokenize(sent.text)]
        chunk.append(tokens)

    entities = []
    for markup in morph.map(chunk):
        found_token_idx = []
        for idx, token in enumerate(markup.tokens):
            if token.tag != 'NUM': continue
            found_token_idx += [idx]
            
        for idx in found_token_idx:
            t = markup.tokens[idx]
            if "." in t.text or "," in t.text: continue # float'ы не берем пока 
            e = NumericEntity(t.text)
            
            for i in range(min(5, len(markup.tokens)-idx)):
                next_t = markup.tokens[idx+i]
                if next_t.pos == 'SYM' and next_t.text == "%":
                    e.pct = True
                elif next_t.pos == 'NOUN' and next_t.feats['Number'] == 'Plur':
                    e.update_entity(entity=next_t.text, normal_form=morph_analyzer.parse(next_t.text)[0].normal_form)
                    break
            entities += [e]
    return entities


def process_entities(entities):
    img_name = "myapp/graphics/img.png"
    percentages_ent = [e for e in entities if e.pct]
    obj_ent = [e for e in entities if not e.pct]
    if len(percentages_ent) / len(entities) > 0.5:
        data = []
        labels = []
        for p in percentages_ent:
            try:
                data.append(int(p.number))  # Изменено на append
                labels.append(p.normal_form)  # Изменено на append
            except:
                print("convertation error, skipping this one")
        # labels = [p.normal_form for p in percentages_ent]
        preset_pie(data, labels, img_name)
    else:
        data = []
        labels = []
        for p in obj_ent:
            try:
                data.append(int(p.number))  # Изменено на append
                labels.append(p.normal_form)  # Изменено на append
            except:
                print("convertation error, skipping this one")
        # labels = [p.normal_form for p in obj_ent]
        preset_barplot(data, labels, img_name)

    return img_name


### --------------------- FULL LOGIC --------------------- ###
class LanguageProcessor(object):
    def __init__(self):
        self.morph_analyzer = pymorphy2.MorphAnalyzer()

        current_dir = os.path.dirname(__file__)  # Текущий каталог
        navec_path = os.path.join(current_dir, 'nlp_assets', 'navec_news_v1_1B_250K_300d_100q.tar')
        morth_path = os.path.join(current_dir, 'nlp_assets', 'slovnet_morph_news_v1.tar')

        self._navec = Navec.load(navec_path)
        self.morph = Morph.load(morth_path, batch_size=4)
        self.morph.navec(self._navec)

    def process(self, texts):
        summarized_sentences = process_text(texts)
        keywords = get_keywords(texts, self.morph_analyzer)
        entities = extract_numeric_entities(texts, self.morph, self.morph_analyzer)
        if len(entities) > 0:
            img_name = process_entities(entities)
        else: img_name = None

        return {
            1:{
                "text": summarized_sentences[:len(summarized_sentences) // 2],
                "path": None
            },
            2:{
                "text": summarized_sentences[len(summarized_sentences) // 2:],
                "path": None
            },
            3:{
                "text": None,
                "path": img_name
            },
        }
  

if __name__ == '__main__':
    lp = LanguageProcessor()
    with open("nlp_assets/text.txt", 'r', encoding='utf-8') as f:
        text = f.read()

    result = lp.process(text)
    print(result)