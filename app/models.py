from django.db import models



class BaseModel(models.Model):
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        verbose_name = "Base Model"
        verbose_name_plural = "Base Models"


class Specialization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Specialization"
        verbose_name_plural = "Specializations"


class Award(models.Model):
    image = models.ImageField(upload_to='images/')
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Award"
        verbose_name_plural = "Awards"



class AwardWinner(models.Model):
    portfolio = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    competition_name = models.CharField(max_length=255)
    specialization = models.ForeignKey(
        Specialization, related_name='award_winners', on_delete=models.CASCADE
    )
    award = models.ForeignKey(
        Award, related_name='awards', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Award Winner"
        verbose_name_plural = "Award Winners"


class Review(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "AReviews"


class Service(models.Model):

    class ServiceStatus(models.Choices):
        pass

    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)
    status = models.CharField()
    parent = models.CharField()

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class WebSiteService(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='images/')
    order = models.IntegerField(default=0)
    file = models.FileField()
    parent = models.CharField()

    class Meta:
        verbose_name = "Web Site Service"
        verbose_name_plural = "Web Site Services"


class ApplicationType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Application Type"
        verbose_name_plural = "Application Type"


class Application(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"


class SEOAnalytic(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    file = models.FileField()
    icon = models.ImageField(upload_to='images/')
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "SEO Analytic"
        verbose_name_plural = "SEO Analytics"


class Feat(models.Model):
    icon = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Feat"
        verbose_name_plural = "Feats"


class Portfolio(models.Model):
    poster = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    feat = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class ProjectProgress(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    portfolio = models.ForeignKey(
        Portfolio, related_name='project_progresses', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Project Progress"
        verbose_name_plural = "Project Progress"


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Article"































