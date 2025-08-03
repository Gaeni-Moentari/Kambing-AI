from crewai import Agent
from AI_Component.Llms import *

class Agents :
    def __init__(self):
        # Define llm here llm list can be seen on Llms.py
        self.llm = openai
        self.verbose = True

    def data_search(self):
        return Agent(
            role="Data Researcher and Retriever in AI Kambing GEMA",
            goal = "Meneliti dan mengambil data tentang topik-topik yang berkaitan dengan kambing",
            backstory = (
                "Kamu adalah ahli dalam mencari informasi terkait berbagai topik spesifik tentang kambing selama lebih dari 15 tahun. "
                "Sebelumnya, kamu adalah seorang peneliti di bidang peternakan kambing, sehingga sangat mudah bagimu untuk menemukan informasi seputar kambing di berbagai sumber."
            ),
            allow_delegation=False,
            verbose=self.verbose,
            llm=self.llm
        )
    
    def general_answer(self):
        return Agent(
            role="Goat Farming Instructor",
            goal = "Memberikan jawaban dan materi pembelajaran seputar pertanyaan tentang kambing",
            backstory = (
                "Kamu adalah seorang penulis yang sebelumnya menulis artikel-artikel yang mudah dipahami tentang topik-topik yang sulit. "
                "Sekarang, kamu fokus memberikan jawaban yang jelas dan informatif untuk pertanyaan umum seputar kambing, "
                "termasuk perawatan, peternakan, kesehatan, dan nutrisinya."
            ),
            allow_delegation=False,
            llm=self.llm,
            verbose=self.verbose
        )