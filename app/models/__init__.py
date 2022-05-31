from app.models.hugging_face_models import HuggingFaceChatBot

_cache = {}


def chatbot_factory(configs: dict):
    model_name = configs.get('model_name')

    if model_name in _cache:
        return _cache[model_name]

    if model_name:
        chatbot = HuggingFaceChatBot(model_name=model_name)
        _cache[model_name] = chatbot
        return chatbot
    else:
        raise NotImplementedError
