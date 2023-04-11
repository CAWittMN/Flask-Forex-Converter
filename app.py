from flask import Flask, redirect, request, render_template, requests
app = Flask(__name__)

apiURL = 'https://api.exchangerate.host/convert'