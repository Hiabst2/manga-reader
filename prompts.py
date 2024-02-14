BASIC_PROMPT = """
I am giving you the character profiles of manga characters, the story so far, and then a sequence of pages directly out of a manga.
I want you to continue the story were it left off after the "story so far" that includes the new sequence of pages that I have provided. 
Please write me a summary of all the pages in a story-telling tone. 
I don't want you to invent new things, just summarize what is happening in the pages provided. 
Also, include some direct quotes from particularly intense parts in your storytelling.

Your final summary should stick to the plot without over embellishing. The end product should be a script that can be read in a short 1-minute highlight reel of the manga."""

BASIC_PROMPT_WITH_CONTEXT = """
Pasted above is a summary of the chapters up to this point in the volume, just to give you some context.
Your job is to summarize the sequence of pages out of the manga in a compelling, storytelling tone. Don't be long-winded and stick to the plot. 
The end-result should be able to be read in less than a minute of time.
Please strive to sprinkle in some direct quotes from particularly intense parts to enhance your storytelling.
"""

DRAMATIC_PROMPT = """
I am giving you the character profiles of manga characters, the story so far, and then a sequence of pages directly out of a manga.
I want you to continue the story were it left off after the "story so far" that includes the new sequence of pages that I have provided. 
Please write me a summary of all the pages in an engaging, story-telling tone. 
I don't want you to invent new things, just summarize what is happening in the pages provided. 
Also, include some direct quotes from particularly intense parts in your storytelling.
"""

CHAIN_OF_DENSITY_PROMPT = """
Pasted above is a summary of the chapters up to this point in the volume. 
I'm also uploading a sequence of pages from a new chapter that hasn't been incorporated into the summary yet, directly from the manga.
I want you to incorporate the new chapter into the existing summary I gave you, while maintaining the same summary length.
The result should be a summary of all of the chapters including the new one I gave you, that is roughly the same length as the summary above.

To help you with the summary task, I am uploading an image of the character profiles of manga characters and then a sequence of pages from the next chapter for you to summarize.
Please incorporate a summary of all the pages in an engaging, story-telling tone, without leaving out important moments and highlights.
I don't want you to invent new things, just incorporate what is happening in the pages provided into the running summary above. 
Also, include some direct quotes from particularly intense parts in your storytelling.

REMEMBER: Your summary should INCLUDE the summary of the chapters up to this point AND the new chapter I gave you, without losing important details from the previous summary.
IT IS A MATTER OF LIFE OR DEATH that you be careful to not exclude important details from the previous chapters' summary.
The end goal is to have a concise, engaging highlight story of ALL the chapters, including the new chapter I gave you.
Please remember to retain direct quotes from particularly intense parts in your storytelling.
"""

BASIC_INSTRUCTIONS = """Your job is to summarize the sequence of pages out of the manga in a compelling, storytelling tone. Don't be long-winded and stick to the plot. 
The end-result should be able to be read in less than a minute of time.
Please strive to sprinkle in some direct quotes from particularly intense parts to enhance your storytelling."""


