from django.db import models
from django.contrib.auth.models import User
from general.models import GeneralModel 


class Ticket(GeneralModel):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
        ('on_hold', 'On Hold'),
    ]
    
    subject = models.CharField('Subject', max_length=200)
    description = models.TextField('Description', blank=True, null=True)
    priority = models.CharField('Priority', max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField('Status', max_length=30, choices=STATUS_CHOICES, default='open')
    assigned_to = models.ForeignKey(User, related_name='tickets_assigned', on_delete=models.SET_NULL, null=True, blank=True)
    closed_at = models.DateTimeField('Closed At', blank=True, null=True)
    category = models.ForeignKey('Category', related_name='tickets', blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Tags')

    def __str__(self):
        return f'{self.id}-{self.subject}'

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['create_at']

class Category(GeneralModel):
    name = models.CharField('Category Name', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

class Tag(GeneralModel):
    name = models.CharField(max_length=200, unique=True, verbose_name='Tag Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']
        

class Profile(GeneralModel):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    
    


class TicketConversation(GeneralModel):
    
    
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed','Closed'),
        ]
    
    customer = models.ForeignKey(User, related_name='conversations', on_delete=models.CASCADE)
    operator = models.ForeignKey(User, related_name='handled_conversations', on_delete=models.CASCADE)
    subject = models.CharField('Subject', max_length=100)
    status = models.CharField('Status', max_length=30 ,choices=STATUS_CHOICES, default='open')
    tickets = models.ManyToManyField(Ticket, related_name='conversations')
    started_at = models.DateField('Started At', auto_now_add=True)
    ended_at = models.DateTimeField('Ended At', null=True, blank=True)

    def __str__(self):
        return f'{self.customer}-{self.operator}-{self.subject}-{self.status}-{self.tickets}-{self.started_at}'
    class Meta:
        verbose_name = 'TicketConversation'
        verbose_name_plural = 'TicketConversations'
        ordering = ['subject']