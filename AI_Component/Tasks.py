from crewai import Task
from AI_Component.Agents import *
from AI_Component.Tools import *


agents = Agents()

class Tasks:
    def __init__(self, input, lang):
        self.input=input
        self.lang=lang
    def general_search_task(self):
        return Task(
            description=f"Tugas kamu adalah mencari data seputar informasi tentang kambing berdasarkan input: {self.input}, "
                        "beserta dengan link referensinya. "
                        "Kamu akan memberikan hasil pencarianmu kepada penulis jawaban. "
                        "Kamu akan menggunakan alat [WebSearch].",
            expected_output="Sebuah hasil pencarian yang lengkap dari berbagai sumber dengan link sumbernya. "
                            "Gunakan format yang mudah dipahami sebagai bahan untuk menyusun jawaban yang komprehensif.",
            agent=agents.data_search(),
            tools=[WebSearch]
        )

    def general_answer_task(self):
        return Task(
            description="Tugas kamu adalah: "
                        f"Menjawab pertanyaan seputar kambing berikut: {self.input}. "
                        "Gunakan data yang telah dicari sebelumnya. "
                        "Sertakan link referensi yang mendukung jawabanmu dari informasi yang disediakan.",
            expected_output="Jawaban dibuat dalam format markdown seperti ringkasan Wikipedia singkat. "
                            "Jawaban menyertakan referensi yang bisa dikunjungi di akhir. "
                            f"Jawaban HARUS menggunakan bahasa berikut: {self.lang}.",
            agent=agents.general_answer()
        )
