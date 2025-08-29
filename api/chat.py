import json

def handler(request):
    try:
        body = json.loads(request.body)
        message = body.get("message", "")
        personality = body.get("personality", "friendly")

        # Simple personality-based response logic
        responses = {
            "friendly": f"Hey there! 😊 You said: '{message}'",
            "formal": f"Greetings. 🤵 You mentioned: '{message}'",
            "funny": f"LOL 😂 Did you really say: '{message}'?",
            "humorous": f"🧠 Processing wait... '{message}' received!",
        }

        reply = responses.get(personality.lower(), f"🤖 Echo: '{message}'")

        return {
            "statusCode": 200,
            "body": json.dumps({ "reply": reply })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({ "reply": f"Error: {str(e)}" })
        }