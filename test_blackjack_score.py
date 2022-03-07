from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Right assert statement here
  assert score == 7

# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  hand = [3, 4,"Jack"]
  score = blackjack_score(hand)
  assert score == 17


# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = [2, 3,"Ace"]
  score = blackjack_score(hand)
  print (score)
  assert score == 16



# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand = [8, 7,"Ace"]
  score = blackjack_score(hand)
  print (score)
  assert score == 16
  # pass

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  hand = [13, 7,"Ace"]
  score = blackjack_score(hand)
  print (score)
  assert score == "invalid"
  # pass


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  hand = [2, 7,"Ace", 3 , 4 , 5]
  score = blackjack_score(hand)
  print (score)
  assert score == "invalid"
  # pass

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  hand = [2, 7,"Jack", 3 , 4 ]
  score = blackjack_score(hand)
  print (score)
  assert score == "bust"
  pass