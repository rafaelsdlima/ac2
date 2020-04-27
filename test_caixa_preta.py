import os
import subprocess

def test_soma():
    #arrange
    expectation = 2
    
    #act
    path = os.path.dirname(os.path.realpath(__file__))
    with subprocess.Popen(["python3", "main.py", "+"], cwd=path,
    stdout=subprocess.PIPE) as p:
        result = p.stdout.read()

    #assert
    assert int(result.decode("utf-8")) == expectation

def test_subtracao():
    #arrange
    expectation = 0

    #act
    path = os.path.dirname(os.path.realpath(__file__))
    with subprocess.Popen(["python3", "main.py", "-"], cwd=path,
    stdout=subprocess.PIPE) as p:
        result = p.stdout.read()
            

    #assert
    assert int(result.decode("utf-8")) == expectation

def test_multiplicacao():
    #arrange
    expectation = 1

    #act
    path = os.path.dirname(os.path.realpath(__file__))
    with subprocess.Popen(["python3", "main.py", "*"], cwd=path,
    stdout=subprocess.PIPE) as p:
        result = p.stdout.read()
            

    #assert
    assert int(result.decode("utf-8")) == expectation

def test_divisao():
    #arrange
    expectation = 2

    #act
    path = os.path.dirname(os.path.realpath(__file__))
    with subprocess.Popen(["python3", "main.py", "/"], cwd=path,
    stdout=subprocess.PIPE) as p:
        result = p.stdout.read()
            

    #assert
    assert int(result.decode("utf-8")) == expectation
