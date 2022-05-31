import abc


class AbstractBaseChatBot(abc.ABC):
    def get_reply(self, user_message: str) -> str:
        raise NotImplementedError
