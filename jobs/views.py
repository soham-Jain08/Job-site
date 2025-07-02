from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from bookmarks.models import *

# Create your views here.
def job_list(request):
    jobs = Job.objects.filter(is_active=True).select_related('company', 'category')

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(company__name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Filter by category
    category_slug = request.GET.get('category', '')
    if category_slug:
        jobs = jobs.filter(category__slug=category_slug)

    # Filter by employment type
    employment_type = request.GET.get('employment_type', '')
    if employment_type:
        jobs = jobs.filter(employment_type=employment_type)

    # Filter by location
    location = request.GET.get('location', '')
    if location:
        jobs = jobs.filter(location__icontains=location)

    # Pagination
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': JobCategory.objects.all(),
        'employment_types': Job.EMPLOYMENT_TYPES,
        'search_query': search_query,
        'selected_category': category_slug,
        'selected_employment_type': employment_type,
        'selected_location': location,
    }
    return render(request, 'landing.html', context)

def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug, is_active=True)

    # Check if user has bookmarked this job
    is_bookmarked = False
    if request.user.is_authenticated:
        is_bookmarked = JobBookmark.objects.filter(user=request.user, job=job).exists()

    # Get related jobs
    related_jobs = Job.objects.filter(
        category=job.category,
        is_active=True
    ).exclude(id=job.id)[:5]

    context = {
        'job': job,
        'is_bookmarked': is_bookmarked,
        'related_jobs': related_jobs,
    }
    return render(request, 'jobs/job_detail.html', context)
