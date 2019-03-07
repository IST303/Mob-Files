import pytest

def ftoc(f):
       
    if f < -459.67: 
        raise exception("You can't go below abs 0, yo!")
    return 5/9*(f-32)


def test_abs0():
        with pytest.raise(exception):
            ftoc(-500)

    
@pytest.mark.parametrize('f,c', [
            (212,100), (-40,-40)])
    

def test_ftoc(f,c):
        assert ftoc(f)==c

    

    
