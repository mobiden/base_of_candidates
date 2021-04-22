from django.db import models

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
    mob_phone = models.BigIntegerField(
                                    null=True,
                                    blank=True,
                                    unique=True,
                                    )

    sec_phone = models.IntegerField(blank=True, null=True,)

    e_mail = models.EmailField(
                                    null=True,
                                    blank=True,
                                    unique=True)
    city = models.CharField(max_length=45,
                            default='Moscow',
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
    current_company = models.ForeignKey('Company', models.SET_NULL,
                                    blank=True,
                                    null=True,
                                        )
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


class Project(models.Model):
    vacancy = models.CharField(max_length= 120,
                               null=True,
                               blank=True,
                               )
    project_name = models.CharField(max_length=120,
                                    null=True,
                                    blank=True,
                                    )
    persons = models.ManyToManyField('Person',
                                     related_name='long_list_persons',
                                    )
    client = models.ForeignKey('Company', models.SET_NULL,
                                    blank=True,
                                    null=True,
                               )
    comments = models.TextField(blank=True,
                            null=True,
                                )

class Company(models.Model):
    company_name = models.CharField(max_length=45,
                                    primary_key= True,
                                    )
    city = models.CharField(max_length=45,
                            null=True,
                            blank=True,
                            )
    phone = models.BigIntegerField(
        null=True,
        blank=True,
    )

