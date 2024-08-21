from src.utils import get_gdp

if __name__ == '__main__':
    gdp = get_gdp('China', 2023)
    print(gdp['answer_box']['snippet'])