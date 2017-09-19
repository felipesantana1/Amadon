# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request,'amadon_app/index.html')

def process(request):

    request.session['total'] = 0
    if 'count' not in request.session:
        request.session['count'] = 0

    if 'overall' not in request.session:
        request.session['overall'] = 0

    if request.POST['id'] == '101':
        price = 19.99 * int(request.POST['amount'])
        request.session['total'] += price
        request.session['count'] +=  int(request.POST['amount'])
        request.session['overall'] += price

    if request.POST['id'] == '102':
        price = 29.99 *  int(request.POST['amount'])
        request.session['total'] += price
        request.session['count'] +=  int(request.POST['amount'])
        request.session['overall'] += price

    if request.POST['id'] == '103':
        price = 4.99 *  int(request.POST['amount'])
        request.session['total'] += price
        request.session['count'] +=  int(request.POST['amount'])
        request.session['overall'] += price

    if request.POST['id'] == '104':
        price = 49.99 *  int(request.POST['amount'])
        request.session['total'] += price
        request.session['count'] +=  int(request.POST['amount'])
        request.session['overall'] += price

    return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon_app/success.html')

def goBack(request):
    return redirect('/')