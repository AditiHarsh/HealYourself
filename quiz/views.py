from django.shortcuts import render
import pickle

# Create your views here.
def quiz(request):
    return render(request,"quizIndex.html")

def getPredictions(email,name,gender,employment,city,feel,ifsad,sleep,stress,sadness,daytime,suddenchange,littlepleasure,support,doingthings,medicalleave,abuse,cry,affect,sleeptime,failure,concentrate,therapy,lonely,talk,confidence,appoint):
    model = pickle.load(open('baaamodel_.sav','rb'))
    scaled = pickle.load(open('_scaler.sav','rb'))

    prediction = model.predict(scaled.transform(
        email,name,gender,employment,city,feel,ifsad,sleep,stress,sadness,daytime,suddenchange,littlepleasure,support,doingthings,medicalleave,abuse,cry,affect,sleeptime,failure,concentrate,therapy,lonely,talk,confidence,appoint
    ))

    if prediction<=0.5:
        return 'Mental Aid not needed'
    else:
        return 'Mental Aid needed'

def result(request):
    email=request.GET['email']
    name=request.GET['name']
    gender=request.GET['gender']
    employment=request.GET['employment']
    city=request.GET['city']
    feel=request.GET['feel']
    ifsad=request.GET['ifsad']
    sleep=request.GET['sleep']
    stress=request.GET['stress']
    sadness=request.GET['sadness']
    daytime=request.GET['daytime']
    suddenchange=request.GET['suddenchange']
    littlepleasure=request.GET['littlepleasure']
    support=request.GET['support']
    doingthings=request.GET['doingthings']
    medicalleave=request.GET['medicalleave']
    abuse=request.GET['abuse']
    cry=request.GET['cry']
    affect=request.GET['affect']
    sleeptime=request.GET['sleeptime']
    failure=request.GET['failure']
    concentrate=request.GET['concentrate']
    therapy=request.GET['therapy']
    lonely=request.GET['lonely']
    talk=request.GET['talk']
    confidence=request.GET['confidence']
    appoint=request.GET['appoint']

    result = getPredictions(email,name,gender,employment,city,feel,ifsad,sleep,stress,sadness,daytime,suddenchange,littlepleasure,support,doingthings,medicalleave,abuse,cry,affect,sleeptime,failure,concentrate,therapy,lonely,talk,confidence,appoint)


    return render(request,"result.html",{'result': result})