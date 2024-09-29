from django.shortcuts import render

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit):
    return [num for num in range(2, limit + 1) if is_prime(num)]

def prime_numbers_view(request):
    primes = []
    number = None
    if request.method == 'POST':
        number = int(request.POST.get('number', 0)) 
        primes = get_primes(number)  

    return render(request, 'primes/prime_numbers.html', {'primes': primes, 'number': number})  
