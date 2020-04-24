import os
import subprocess


def test_soma():

    #arrange
    expectation = 2

    #act
    path = os.path.dirname(os.path.realpath(__file__))
    with subprocess.Popen(["python3", "calculadora.py", "soma"] cwd=path, stdout=subprocess.PIPE) as p:
        result = p.stdout.read()

    #assert
    assert int(result.decode("utf-8")) == expectation


def test_subtrai():
    expectation = 0

    path = os.path.dirname(os.path.realpath(__file__))
    with subprocess.Popen(["python3", "calculadora.py", "subtracao"] cwd=path, stdout=subprocess.PIPE) as p:
        result = p.stdout.read()

    #assert
    assert int(result.decode("utf-8")) == expectation

