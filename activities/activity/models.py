from django.db import models


class Who(models.Model):
    who = models.CharField(max_length=250,
                              null=False, blank=False, default='')

    def __str__(self):
        return f"Who: {self.who}"


class Activity(models.Model):

    status_choice = [
    ("TODO", "To do"),
    ("DOING", "Doing"),
    ("DONE", "Done")
    ]

    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    initial_date = models.DateTimeField()
    end_date = models.DateTimeField()
    who = models.ForeignKey(Who, on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=status_choice)

    def __str__(self):
        return f"Activity: {self.title} | End date: {self.end_date} | Responsible: {self.who}"
