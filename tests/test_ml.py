from api.ml import ml_main

def test_ml_main(filepath,target):
    eval=ml_main(filepath,target,split =0.3)
    assert eval == 'MSE =  45.88,  MAE = 5.373'