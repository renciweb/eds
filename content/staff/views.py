from django.shortcuts import get_object_or_404, render

from .models import StaffMember

def index(request):
    staff_members = StaffMember.objects.all()
    context = {
        'page_title': 'Staff',
        'staff': staff_members
    }
    return render(request, 'staff/index.html', context)

def detail(request, staff_slug):
    staff_member = get_object_or_404(StaffMember, slug=staff_slug)
    projects = staff_member.project_set.all()
    publications = staff_member.publication_set.all()
    context = {
        'page_title': staff_member.display_name,
        'staff_member': staff_member,
        'projects': projects,
        'publications': publications,
    }
    return render(request, 'staff/detail.html', context)