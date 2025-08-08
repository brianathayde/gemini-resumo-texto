import json
from google import genai


EXEMPLO_AVALIACAO_PRODUTO = """
    Comprei este fone de ouvido sem fio há duas semanas e
     estou bastante impressionado.
    A qualidade do som é fantástica, com graves profundos e agudos
     cristalinos, superou minhas
    expectativas para um produto nessa faixa de preço. O cancelamento de ruído
     ativo funciona
    muito bem em ambientes como ônibus e escritórios. A bateria também dura
     bastante, consigo
    usar por quase 3 dias sem precisar recarregar. O único ponto negativo é
     que ele aperta
    um pouco a orelha depois de umas 3 horas de uso contínuo, o que pode ser
     desconfortável.
    Mas, no geral, o custo-benefício é excelente. Recomendo!
    """


def resumirAvaliacao(avaliacao: str, api_key: str) -> str:
    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
        Resuma a seguinte avaliação de produto de forma objetiva, destacando
         os pontos principais.
        O resumo final deve ter no máximo 150 caracteres.

        Avaliação:
        '''
        {avaliacao}
        '''

        Resumo conciso:
        """

        response = client.models.generate_content(
            model = "gemini-2.5-flash", 
            contents = prompt
        )

        return response.text.strip()

    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API: {e}")
        return "Não foi possível gerar o resumo."


with open('config.json', 'r') as arquivo:
    config = json.load(arquivo)
    GEMINI_API_KEY = config['apiKey']

    resumo = resumirAvaliacao(EXEMPLO_AVALIACAO_PRODUTO, GEMINI_API_KEY)

    print("--- Avaliação Original ---")
    print(EXEMPLO_AVALIACAO_PRODUTO)
    print("\n" + "="*40 + "\n")
    print("--- Resumo Gerado (Máx 150 caracteres) ---")
    print(resumo)
    print(f"\nComprimento do resumo: {len(resumo)} caracteres")
