
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def contact_submit(request):

    if request.method == "POST":

        # Honeypot spam protection
        if request.POST.get("website", "").strip():
            return redirect("home")

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

            return redirect("home")

        messages.error(
            request,
            "Please correct the errors in the contact form."
        )

    else:
        form = ContactForm()

    return render(
        request,
        "core/contact.html",
        {"form": form}
    )
