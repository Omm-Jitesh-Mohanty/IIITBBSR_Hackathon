from django.db import models

# Create your models here.
# from django.db import models


class BriefingSession(models.Model):

    question = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        default="processing"
    )


class Document(models.Model):

    session = models.ForeignKey(
        BriefingSession,
        on_delete=models.CASCADE
    )

    file = models.FileField(upload_to="documents/")

    uploaded_at = models.DateTimeField(auto_now_add=True)


class GeneratedSlides(models.Model):

    session = models.OneToOneField(
        BriefingSession,
        on_delete=models.CASCADE
    )

    ai_output = models.TextField()


class Presentation(models.Model):

    session = models.OneToOneField(
        BriefingSession,
        on_delete=models.CASCADE
    )

    ppt_file = models.FileField(upload_to="presentations/")