from django.shortcuts import render, reverse

from ..auth.decorators import login_required, teacher_or_superuser_required

# Create your views here.

@teacher_or_superuser_required
def index_view(request):
    return render(
        request,
        "docs/index.html",
        {
            "docs_app": True,
            "pages": {
                reverse("docs:graders"): "Graders",
            },
        },
    )

@teacher_or_superuser_required
def graders_view(request):
    return render(request, "docs/graders.html", {"docs_app": True, "nav_item": "Graders"})

