
from django.shortcuts import render
from .services.pdf_reader import extract_text_from_pdf
from .services.ai_generator import generate_slide_content
from .services.ppt_generator import create_ppt


def index(request):

    ai_output = None
    ppt_file = None

    if request.method == "POST":

        files = request.FILES.getlist("documents")
        question = request.POST.get("question")

        extracted_text = ""

        for file in files:
            text = extract_text_from_pdf(file)
            extracted_text += text

        print("EXTRACTED TEXT:")
        print(extracted_text)
        ai_output = generate_slide_content(extracted_text[:4000], question)

        print("AI OUTPUT:")
        print(ai_output)

        ppt_file = create_ppt(ai_output)

    context = {
        "output": ai_output,
        "ppt_file": ppt_file
    }

    return render(request, "index.html", context)