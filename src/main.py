"""
EuroPython 2022 - Cloud Challenge - Participant
Copyright 2022 Google LLC.
SPDX-License-Identifier: Apache-2.0
"""
import flask


def cloud_challenge_data(_: flask.Request) -> flask.Response:
    """Cloud Function returning your Cloud Challenge data."""
    # 1. Answer to the ultimate question (yes, that's the correct answer)
    ANSWER = 42
    # 2. Your current status (pick one emoji)
    STATUS = "🚀"  # 🚀👍🥰🎉🔴🟠🟡🟢🔵
    # 3. Name on your badge
    NAME = "Siobhán Fáilte"
    # 4. Order number on your badge (5 alpha-numeric chars in bottom-left corner)
    ORDER_NUMBER = "XXXXX"
    # 5. Are you eligible to participate in the raffles? (set to False if you're a Googler)
    ELIGIBLE = True

    data = dict(
        answer=ANSWER,
        status=STATUS,
        name=NAME,
        order_number=ORDER_NUMBER,
        eligible=ELIGIBLE,
    )

    return flask.jsonify(data)
