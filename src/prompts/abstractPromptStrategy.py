import abc


class AbstractPromptStrategy:
    """
    Represents a strategy for generating prompts for a given audio segment.

    Note that the strategy must be picklable, as it will be serialized and sent to the workers.
    """
    
    @abc.abstractmethod
    def get_segment_prompt(self, segment_index: int, whisper_prompt: str, detected_language: str) -> str:
        """
        Retrieves the prompt for a given segment.

        Parameters
        ----------
        segment_index: int
            The index of the segment.
        whisper_prompt: str
            The prompt for the segment generated by Whisper. This is typically concatenated with the initial prompt.
        detected_language: str
            The language detected for the segment.
        """
        pass

    @abc.abstractmethod
    def on_segment_finished(self, segment_index: int, whisper_prompt: str, detected_language: str, result: dict):
        """
        Called when a segment has finished processing.
        
        Parameters
        ----------
        segment_index: int
            The index of the segment.
        whisper_prompt: str
            The prompt for the segment generated by Whisper. This is typically concatenated with the initial prompt.
        detected_language: str
            The language detected for the segment.
        result: dict
            The result of the segment. It has the following format:
                {
                    "text": str,
                    "segments": [
                        {
                            "text": str,
                            "start": float,
                            "end": float,
                            "words": [words],
                        }
                    ],
                    "language": str,
                }
        """
        pass

    def _concat_prompt(self, prompt1, prompt2):
        """
        Concatenates two prompts.

        Parameters
        ----------
        prompt1: str
            The first prompt.
        prompt2: str
            The second prompt.
        """
        if (prompt1 is None):
            return prompt2
        elif (prompt2 is None):
            return prompt1
        else:
            return prompt1 + " " + prompt2