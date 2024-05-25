from flask import Flask, render_template, redirect, request, url_for


@app.route('/')
def test3():
	return 'This is Home!123123123123'
