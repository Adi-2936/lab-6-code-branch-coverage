from password_policy import check_password, strength, suggest_fix


def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []


def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"


# Original starter tests from the assigned repository.
