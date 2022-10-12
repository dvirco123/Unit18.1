from flask import Flask, request, render_template, redirect, flash, session
app=Flask(__name__)

app.config['SECRET_KEY'] ="progress0402"
