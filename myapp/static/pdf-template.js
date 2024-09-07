document
  .getElementById("replaceTextButton")
  .addEventListener("click", async () => {
    const fileInput = document.getElementById("fileInput");

    if (fileInput.files.length === 0) {
      alert("Please select a PDF file");
      return;
    }

    const pdfFile = fileInput.files[0];
    const arrayBuffer = await pdfFile.arrayBuffer();
    const { PDFDocument, rgb } = PDFLib;

    const replacements = {
      "Текст": "New Text",
      "Another Old Text": "Another New Text",
    };

    const pdfDoc = await PDFDocument.load(arrayBuffer);
    const pages = pdfDoc.getPages();

    for (const page of pages) {
      const { width, height } = page.getSize();

      page.drawRectangle({
        x: 50,
        y: height - 100,
        width: 200,
        height: 30,
        color: rgb(1, 1, 1),
      });

      page.drawText("New Text", {
        x: 50,
        y: height - 100,
        size: 30,
        color: rgb(0, 0, 1),
      });
    }

    const pdfBytes = await pdfDoc.save();

    const blob = new Blob([pdfBytes], { type: "application/pdf" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "updated.pdf";
    link.click();
  });
