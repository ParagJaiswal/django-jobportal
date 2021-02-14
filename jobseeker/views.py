from django.shortcuts import render

def index(request):
	return render(request,'jobseeker/index.html')


def hr(request):
	return render(request,'jobseeker/hr.html')

def candidate(request):
	return render(request,'jobseeker/candidate.html')