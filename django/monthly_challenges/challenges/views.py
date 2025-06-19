from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for atleast 20 minutes every day!',
    'march': 'Learn Django for atleast 20 minutes every day!',
    'april': 'Learn Django for atleast 20 minutes every day!',
    'may': 'Learn Django for atleast 20 minutes every day!',
    'june': 'Learn Django for atleast 20 minutes every day!',
    'july': 'Eat no meat for the entire month',
    'august': 'Walk for atleast 20 minutes every day!',
    'september': 'Learn Django for atleast 20 minutes every day!',
    'october': 'Learn Django for atleast 20 minutes every day!',
    'november': 'Learn Django for atleast 20 minutes every day!',
    'december': 'use Django for web development.'
}


def index(request):

    months = list(monthly_challenges.keys())

    return render(request,'challenges/index.html', {'months': months})

    # OR build the html by concatenating strings to form the element
    # list_items = ""

    # # we use a loop to write all <li> elements as one string so that we can use the result with <ul>
    # # to create our unordered list element for our response
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse('month-challenge', args=[month])
    #     list_items += f"<li><a href={month_path}>{capitalized_month}</a></li>"

    # # list_items becomes a long string of <li> elements written side by side
    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)


# view functions would be defined here
# returns the response to the browser/client sending the request
def monthly_challenge_by_number(request, month: int):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month - 1]

    # `reverse` allows us to create full path to a specific url using the values we pass to `args`
    # we construct the path we want to redirect to. -> '/challenges/<month>'
    # the value we get from `redirect_month` is what we append to /challenges/ which is the base url path
    redirect_path = reverse('month-challenge', args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    """
    :param request: request object
    :param month: our dynamic segment identifier name.
    :return: None
    """

    try:
        # we used path converters to convert `month` to str in the url path declaration
        # in order to key index the monthly_challenges dict
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            'text': challenge_text,
            'month_name': month
        })  # the context value is exposed inside our templates

        # OR use render_to_string, here the context value is the second argument
        # response_data = render_to_string("challenges/challenge.html")  # transform the content of the html file to a string
        # return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')
    except:
        return HttpResponseNotFound('<h1>Exception: This month is not supported!</h1>')
