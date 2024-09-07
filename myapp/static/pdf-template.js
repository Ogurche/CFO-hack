function addHtmlToSlide(slide, htmlContent) {
  let htmlElement = document.createElement("div");
  htmlElement.innerHTML = htmlContent;
  let text = htmlElement.innerText || htmlElement.textContent;

  slide.addText(text, {
    x: 0.5,
    y: 0.5,
    w: "90%",
    h: "90%",
    fontSize: 18,
    color: "000000",
  });
}

function loadHtmlFile(file, callback) {
  fetch(file)
    .then((response) => response.text())
    .then((htmlContent) => callback(htmlContent))
    .catch((error) => console.error("Error loading HTML file:", error));
}

function generatePptx(htmlFiles) {
  let pptx = new PptxGenJS();

  htmlFiles.forEach((file) => {
    loadHtmlFile(file, (htmlContent) => {
      let slide = pptx.addSlide();
      addHtmlToSlide(slide, htmlContent);

      if (file === htmlFiles[htmlFiles.length - 1]) {
        pptx.writeFile({ fileName: "presentation.pptx" });
      }
    });
  });
}

document.getElementById("downloadPptx").addEventListener("click", function () {
  let htmlFiles = [
    "./../static/images/city.png",
    "./../templates/slides/page1.html",
    "./../templates/slides/page2.html",
    "./../templates/slides/page3.html",
  ];
  generatePptx(htmlFiles);
});
