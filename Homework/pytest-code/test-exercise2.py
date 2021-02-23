import math

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
    in the sample conpared to the amount in living 
    tissue (unitless). 
    """
    if carbon_14_ratio <= 0:
        return
    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF 

# TODO: Write a unit test which feed 0.35 to the function. 
# The result should be '8680.34'. Does the function handles 
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle 
# every possible input properly. Then write a unit test againt 
# this special case.


def test_carbon_dating():
    """Test the carbon dating function with non zero or negative numbers."""
    assert get_age_carbon_14_dating(0.35) == 8680.34743633106

def test_carbon_dating_with_zero_value():
    """Test the carbon dating function with number of 0."""
    assert get_age_carbon_14_dating(0) == None

def test_carbon_dating_with_negative():
    """Test the carbon dating function with negative numbers."""
    assert get_age_carbon_14_dating(-3) == None