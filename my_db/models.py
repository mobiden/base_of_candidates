from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=60,
                                    null=False,
                                    unique=True,

                                    )
    city = models.CharField(max_length=45,
                            null=True,
                            blank=True,
                            default='Москва',
                            )
    phone = models.CharField(max_length=11,
                             null=True,
                             blank=True,)

    comments = models.TextField(null=True, blank=True)

    creating_date = models.DateTimeField(blank=True, null=True,)

    def __str__(self):
        return self.company_name



class Person(models.Model):
    last_name = models.CharField(max_length=60,
                                null=True,
                                blank=True
                                 )
    first_name = models.CharField(max_length=45,
                                  null=True,

                                  )
    middle_name = models.CharField(max_length=60,
                                   null=True,
                                   blank=True,
                                   )
    mob_phone = models.CharField(max_length=11,
                                    null=True,
                                    blank=True,
                                    unique=True,
                                    )

    sec_phone = models.CharField(max_length=11,
                                    null=True,
                                    blank=True,
                                                     )

    e_mail = models.EmailField(
                                    null=True,
                                    blank=True,
                                    unique=True)

    city = models.CharField(max_length=45,
                            default='Москва',
                            null=True,
                            blank=True,
                            )
    messenger = models.CharField(max_length=45,
                                 null=True,
                                 blank=True,
                                 )
    messenger_id = models.CharField(max_length=120,
                                    null=True,
                                    blank=True,
                                    )
    current_company = models.ForeignKey('Company',
                                        db_column='company_name',
                                        to_field='company_name',
                                        related_name='person_company',
                                        on_delete=models.SET_NULL,
                                    blank=True,
                                   null=True,)

    position = models.CharField(max_length=120,
                                    null=True,
                                    blank=True,
                                    )

    comments = models.TextField(
                                null=True,
                                blank=True,
                                    )
    resume = models.FileField(
                            null=True,
                            blank=True,
                                )
    creating_date = models.DateTimeField( blank=True, null=True)



class Project(models.Model):
    vacancy = models.CharField(max_length= 120,
                               null=True,
                               blank=True,
                               )
    project_name = models.CharField(max_length=120,
                                    null=True,
                                    blank=True,
                                    )

    client = models.ForeignKey('Company',
                               db_column='company_name',
                               to_field='company_name',
                               related_name='client_company',
                                    blank=True,
                                    null=True,
                               on_delete=models.SET_NULL,
                              )
    comments = models.TextField(blank=True,
                            null=True,
                                )
    creating_date = models.DateTimeField(blank=True, null=True,)

    file = models.FileField

class Projects_People(models.Model):
    project = models.ForeignKey('Project',
                                on_delete=models.CASCADE,
                                related_name='long_list_project',)
    people = models.ForeignKey('Person', on_delete=models.CASCADE,
                               related_name='long_list_persons')

    comments = models.TextField(blank=True, null=True)

    STATUS_CHOISES = [
        ('TK', 'to call' ),
        ('II', 'invited for interview'),
        ('IC', 'interview with client'),
        ('CR', 'candidate refused'),
        ('CP', 'candidate to present'),
        ('RS', 'resume sent'),
        ('CV', 'considering vacancy'),

    ]

    status = models.CharField(max_length=2, choices=STATUS_CHOISES,
                              blank=True,
                              null=True,
                            )

