#Model Integration with Web App.py
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)