
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg, Count
from streaming.models import Movie, UserProfile, Review, SubscriptionPlan
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout





def index(request):
    # Query all movies with their average rating and number of ratings
    movies = Movie.objects.annotate(
        average_rating=Avg('reviews__rating'), 
        ratings_count=Count('reviews')
    ).order_by('-average_rating')
    
    # Pass the movies queryset to the template context
    context = {'movies': movies}
    
    # Render the index.html template with the context
    return render(request, 'streaming/index.html', context)

    
def movie(request, movie_id):
    try:
        print(Movie.objects.get(pk=movie_id))
        movie = Movie.objects.get(pk=movie_id)
        return render(request, 'streaming/movie.html', {'movie': movie})
    except ObjectDoesNotExist:
        raise Http404('Movie not found')


def user_reviews(request, user_id):
    user_profile = get_object_or_404(UserProfile, user__id=user_id)
    reviews = Review.objects.filter(user=user_profile)
    return render(request, 'streaming/user_reviews.html', {'reviews': reviews})


def subscription_plan_movies(request, subscription_id):
    subscription_plan = get_object_or_404(SubscriptionPlan, id=subscription_id)
    movies = subscription_plan.movies.all()
    return render(request, 'streaming/subscription_plan.html', {'movies': movies, 'subscription_plan': subscription_plan})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



