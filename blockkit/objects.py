from .components import Component
from .validators import validate_choices, validate_type


class Text(Component):
    MARKDOWN = 'mrkdwn'
    PLAIN = 'plain_text'

    def __init__(self, text, type=MARKDOWN, emoji=None, verbatim=None):
        self._add_field('type', type,
                        [validate_choices([self.PLAIN, self.MARKDOWN])])
        self._add_field('text', text)
        self._add_field('emoji', emoji, [validate_type(bool)])
        self._add_field('verbatim', verbatim, [validate_type(bool)])

    def _validate_emoji(self, emoji):
        if self.type == self.MARKDOWN and emoji:
            raise ValueError(
                f'Emoji field is usable only when type is {self.PLAIN}')
