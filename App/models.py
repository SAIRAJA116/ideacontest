from django.db import models

# Create your models here.


class ProminentParameter(models.Model):
    ppname = models.CharField(max_length=300)
    optimalrange = models.CharField(max_length=300, default=" ")
    units = models.CharField(max_length=50)
    lower_boundary = models.FloatField()
    upper_boundary = models.FloatField()

    def __str__(self):
        return self.ppname


class AtmosCondition(models.Model):
    acname = models.CharField(max_length=300)

    def __str__(self):
        return self.acname


class PondCondition(models.Model):
    pcname = models.CharField(max_length=300)

    def __str__(self):
        return self.pcname


class Combinations(models.Model):
    ppname = models.ForeignKey(ProminentParameter, on_delete=models.CASCADE)
    acname = models.ForeignKey(AtmosCondition, on_delete=models.CASCADE)
    pcname = models.ForeignKey(PondCondition, on_delete=models.CASCADE)
    composition = models.CharField(max_length=500)

    class Meta:
        unique_together = ['ppname', 'acname', 'pcname']

    def __str__(self):
        return str(self.ppname)+" - "+str(self.acname)+" - "+str(self.pcname)+" - "+self.composition
