from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        date = request.POST.get('consultationDate')
        time = request.POST.get('consultationTime')

        # Compose email
        subject = f"New Consultation Request from {first_name} {last_name}"
        body = f"""
        Name: {first_name} {last_name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        Preferred Date: {date}
        Preferred Time: {time}
        """
        send_mail(subject, body, 'officialtopsoftware@gmail.com', ['officialtopsoftware@gmail.com'])
        return JsonResponse({'status': 'success', 'message': 'Form submitted successfully!'})
