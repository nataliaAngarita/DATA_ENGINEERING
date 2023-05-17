import requests
import pandas as pd
import psycopg2



url = "https://api.catboys.com/img"
headers = {"Accept-Encoding": "gzip, deflate"}

response = requests.get(url, headers=headers)
data = response.json()
data

url="data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com"
data_base="data-engineer-database"
user="buitragonatalia778_coderhouse"
with open("C:/DATA ENGINEERING/DATA_ENGINEERING/pwd_coder.txt",'r') as f:
    pwd= f.read()

try:
    conn = psycopg2.connect(
        host='data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com',
        dbname=data_base,
        user=user,
        password=pwd,
        port='5439'
    )
    print("Connected to Redshift successfully!")
    
except Exception as e:
    print("Unable to connect to Redshift.")
    print(e)


df = pd.DataFrame([{'url': 'https://www.zooplus.es/magazine/wp-content/uploads/2017/10/fotolia_103481419-768x512.jpg', 'artist': 'NA', 'source_url': 'NA', 'error':'NA'},{'url': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYVFRgWFRYZGBgaGBoZHBocGhgaGBkcGhgcGhwZGBgcIS4lHB4rHxwYJjgmKy8xNTU1HCQ7QDszPy40NTEBDAwMEA8QHxISHjQkJCs0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NP/AABEIAOEA4QMBIgACEQEDEQH/xAAbAAABBQEBAAAAAAAAAAAAAAAEAAIDBQYBB//EAD8QAAEDAgQDBQYEBQIGAwAAAAEAAhEDIQQSMUEFUWEicYGRoQYTMrHB8EJS0eEUYnKC8RWSByMzNKLSJLPC/8QAGQEAAwEBAQAAAAAAAAAAAAAAAAECAwQF/8QAIREAAgICAwEAAwEAAAAAAAAAAAECESExAxJBURMiYTL/2gAMAwEAAhEDEQA/AC6NYhGU8SoxhV0USF57Z6ASK5ThVQ4YU8NSCghj0Sx6EYEQ0IAnzprqiaGLvu0AMq1A0Ek2CqsNiXYl5y2ptME/mPIdFWe0HFc724el2nF0O7zZo+ZPRafh2CFJjWDYXPM7k95VuPVf0lSthDGwpWpgCUqBkmZLOonFczIAe5657xQOck1A6Jw5SAqFqkBQIeU1cJXJQIeCpGFRApwcgBz6sGFK0qgqY4e8ImQIB6HM4fUeSuqdSyehUPconLr3qIvSBHCV1rk0ldagoklJNlJAiL+HXP4ZGpAICwH+GC5/DI8hchAWCMoKVtJTJxKAsgLIWc9p/aKnh2OYHA1SIDRqJ3J2sp/bDjRw9LsfHUlrT+Ubu8PmV5NWdmJLiSTck3JPMlb8XF2/Zmc+TrhG0/4f4U1alTEvvlOVv9RuT4CB4r0FoXkfsl7S/wAK8seCaTzJj4mO0zDmI1HQePqeGxTXtD2ODmuEgjQhTzRknbK45JrAVlTS1cFRIvWRZwhMITyUkDI8q5lUqQCQHGBPCQCSYDoTCEi5JAjoCSRcmuegDC8KrGpiiw6Z3uPc2f1C3QcvOfZKt/8ANcDYlr/MEesB3qvQw5acm0THKJCUoTJSlZlHSF1oXJXQUAOhJLMuIAlzLudQgrqBEmZczKNcJQBIXrheo8yYXIHRiP8AiOwzSfHZAc2epgrCuMmBuvacfw5lam5rxII8fBeY8W4McNUbLszH/C6PNp5GCF2cMsdTn5Y5sbgeHsIBie/5FXvD+IHDRlzZN2SSI3Itrqs0cdl+Hnp+qjxOKquggwNQGyOpMm5K2klJUzOLayj13C4oPY17TIcJCnzLzn2Y4/VpEMe0upudr+Js6kcwvQmOB0Mrg5ONxZ1RkpIlDk4OTAF1ZljwUpXAkgDspSuAJIA7KRKbK7H3+iaViOPcqDjXtA2jJYWPcyJbMmTmgERtlBM27TRuj+J4mBlBGhk99oAm+4lef8YDHvcymJcXS93Mn8I5kT9wtYwzkicsYKxmKLsS2owZXZmkR+bee/fvXsLAvPvZvgoNYOEuawSTsTM257DwK9DYEc0laSDjTSyOKaU5IrIsYnNTSutQA5JKUkAPAXJSBTHlDEOK4uZl1AxrgoyVMQonNQBLTdLSFmPaDBNqNLH6E9kjUHYj9Fom05O/gn8R4WMgJGms3tylXFvaJdXTPIhw8UifeDMOexG1tlLUrNdDwAA0Wbzj5rSYzCAuIc0hulztN/nM9PKhrcN7Z7RaAdDeNTAI+I2+9FuuS9kOFaDsC2pXfneQ1jtWhomD2gByjyCumY2nRhgcAdfil3Xsj4b/AE5qsolzGOlkwYb4tHacdhtqh6VFjwambM4skkRGa8NE2/FcnkhSbG0lotf9cOUOY5wJkgcxJvfw2RGA9oHl+QjPcXAG/Iju9Vl24V4YHRlDjBBeJIB2nYk6wjOHMd2TOUk5s0BxcGz3wI3VuMayQm7NjX4i8XaxsD4g519JgQNVC7j8G9JwG7swIFt91RY3iOfNF2tBNgYnQgCxOvpuqb/VDXY+YFpcCLWgZgItpfwUKCrRXb+noWB4zRq2Y+/I2NkbUeGgkmANyvIqWLgy0AaRFr6K2Zx2rbMc7fyuuFMuFeDjP6abinH8hinEXlx6RoO8wqyt7TPE5spdrAHZFrb9x8lncXjnVbzLr9ALk2j71QmFwdWo8NaxxcZFgYMXJLtOXmrjGMUQ5NvBd4/GvqCBJOrjrBgAwB0tNyjsLwllFjS/MXv+FhGUQRZz4JJbeQLSn8NYKAALmvqESAIcynBuTs59+4a32vOG4Jzj7ypdxvJuT1nVTKXzRSj6wnhGFyMjc3PerIJBqRC5pO2aISUpQlCBnCkuwkEAJJJJAhFRuddMNcc0vesvJsrUJS0JyS2PCkBTKVRjgYN1DVxIbYXKb4pIO8QmE4UCdlVMr1C7WBOwV22C3tH1VR4V6yHN+ArMWKbpJE964/Fl+sum8D6KHEimL5Mw0lDPqhh7IInaBExrCqUFGOGEZW9FXxw5TYEDkTvt0OqonPL3hrQRa7toIsQPzXJHNXmJaXguzE6wSI32P7DRVNXEQ0imWhxvmdcAxHZIsACSfHcWWcbNXoNoUnBoaIyNzSwAFzp0DyQNRvFjdA4fAMa7MACwEdkNcQXOE5j/ACi1t7rnDKga/wBwSfzBwu5xcBz2mZ3sd1PxQZHMaKjmT8TTBNxJvGvwg625larDoyeclLxB7y9webmALRpAFtAJmw2kolvYazJIySDcyRANudybdSq3HVe23LYOe65M7gyeoReGqVHSxr2DLNnNBBiAY5jr0WvhFguKz+8AOYDUTvcyR4nQp2GptZYTJBJmNdxzaVJiWZ2gPEvbMu0FwLgzfQhA4rGS8ODdBlJO9ss3E3VE6JcM4aZABNpvziT4oz3rIEtEC0RHT5X8Cgq0ZQ8E257SdSBe111lQEaCPv8AdQ0UmTkMYeyxveRO/l/hPfxKo8AOe7LMAA2HKwsBdRsNy3x+ms2U9Og17YFjz+ondS0vS034aL2ewgF3CbjU+vVa5ossd7PVn52ss42k6dnnqtiBCx5Eik2KUkoXQFkUcASTiFG4oA6XJhemOcuIGS50lHCSAMGOMVGGHQ9nLeFPjOMAiWGGkaHYrP46oRlMquZVc9+SdXBdqVZMG/D0L2eD3NJkw4eiuvdBjZJ8VWcEpOa0NOg+4RXGapLLAxyCiUrY1GiuxvEC15DHRa5Q9HjBae24nxsqvOAZe4jn+ydiW0GNDg9zjyOnmmvgMLx3F3uc1rH5QXC37rSVKRLczWyfhJOogXIH7/vnOB0aLrvg95HZutCab3Oze8IGWWiAAIO538eSiTWil9Kp9LPLHOM3JjshoI0AMdypHYd9Os0ZZZmggkEOG8kaG8jvVpx1j6DTXFaGF7WuJaHEAvAJHMgEnwVLxQ1QS9lZr2NLoLwGuIBgOcwaEwLQiMX5ocpIZg8SG4l7Lw0nK6dATOa45fVTcR4hnrF17AnUEToACdYAPmVWUR714kBr3CWuaZa8RMaWO8d6gLHMqFjp3gHuMWGg2VVki8HariHsy6F8xP8ALBm9jFv8o0VAwkjWMvIxcgzz0/dCsb2gSPHqQRIHguVXkmWm+YfUq2JBeKxANPNMkG5HS3zlCVS00mmJcXWJ/KNTaPufB7+HPNPM92RkXJOg3UgxQyAMY4iIBy28J36pJg0BMY/UERpfw15bIkU+Vracu4RpqpKWMLGy9hjuEeY00Qb8WAJbIm958RKrZOg3bnzj6pxJaNY9PVMbWEi/4ST3cu8WSrPEWMiARcjw9ClRVm49icIW0y83LybnWAf1WnKo/ZnGU30Ge7kBogtOrTyPzVs+sFxzb7M2SwTNCkDQq52IT2Ymd1NjoLeFA8rjqiHzSl2Goj3BJsp1NsqR7YCTY6GZklHmSU9w6ni2Mx8wOiI9mKBfW7rqleczpWw9kqeVwA1dclelLETkjmR6Bw6icvaUHHXPDQ1hDBPaPRWWBECTZZn2ixheQ1vd1/ZZI19M5xHHCYIDh0F56quqcQBEFpsn45rWmIdPRJjAWwGT32K2SRDbCeBMdnDiYbItznReh02kszGIADROsAdogzb0WG4bTDO0QRlBNtoEre4miHUWCSwNY27JmSL2Ou+qy5P9Fw0Y3EYptVlTBVnw6czHkCDBtPha3XxpffPpNyV2OECA+Ja4d4sVZ8Qptqj4GgDtX7TmuM22gmNxGqGZjXU+yczm7scDANtJGiuNVRE16Vj8YM7Pd7PacxsBDv1+qtsewVH5ttJvDjoY5rlTJVewBgbBv4dP1VzjsMAxkHUSQIAB6AbfcobV0EU6szwaJsNNrdOnNRVKYa8Hae+/01RL2a84kc7EHwQ+JEgFpHTmeXjAVMEN9pMZdjBdjcriBvy+RU9AscGEPs0yBPQ29UHhMKwuOe/jrtlRtXDYZplrC7oXOA74bdFJitnMW92Jc2jT7RLgSbwB12RXE2MYPdsGYt7Ped+pUdTHVGDJTY2m0i5pt7X+4n1hD4PDnXIRIMuLu1fXfklhaBW3kY7C+5GYOzMIhw5TuosYxrILNJgt5giQZVvWwbGtN4YW5SNuQKp61LIzITmGgPSbd8JWNo1XsYwCXNNrA8x3+v3rrHsWO9jyWGb8nDboR98lsH1wVzc0lZvBOgatTPNSYGhJuU170bw+JlRCKkVKVILZhbKB9KNVbhwhVePqclo4JGcZNsjDgE2pXEIB9ebJ1BuYqXAuyT3iSI/hklP4w7I8QwWEznWFvfY3hocc+wss7w7CNAA5r0DhTG02BjRAi8bldU5eGEI1kuKpAaRubBYPjLwx+VnafvI0Wrx2NaxjnukQIBWQxbie24wXeBI+azTNEiorYkudlyid3foiKGFi5uT1t5LuEwwe4k6Dco99AEctrnbpOq2tIinIKweFljg49lwymIiJFp63HitLx+q4Np02Oa0mLQTItsCPu+iqaLAKIIsA+mCbCe0LDMfXb0R/FsRD2AOAIiZdRkWkNGZ4MkkGwK5+zky2kiqxVJzJPxyIIvBE7jeBNlnuKcPirDMpGvZkwDpJM/st3iKbajMzcoJsHEXJ6OEg/d1V4t9OiA5+rngaSGhrSSSeWt1UZNCaTM0/BOYwutOX8NzAuYI+9Vc1SRTZMNIAF7kdI+vRR1yKpDGn4nNEjQBzhedALG6r/aLijBULGQ9jbZ2mxI+x5KkpSkEnGMQbES50gzyufLXvVbXqQY0JcI/q05/d08cREfCR11Hoh8TVJcwjcn7lbOLRl2QY4OEHLI1sb+RXHOLdJG8D8Q3PJE0Hy0d0EpYnC5mZgSSIM2keeneeqSG/4CsqGPiMXOjpHcYsUXSwr3hpcSGAczPSevVE4bhrg0HPfVoIkDXdOdWcy5eDGtoB/T91LZSXrBMTQcwPYHkjJmaJk+E7qvzFwYCdR82xPoFdB4e0ONrEeZv6Kl4ZSz1WCQQC4WPIHY325IE8Gq4ZRLCCNwPlf1Vp7wrjKcADonZVwTlbOhYRw1SiMNjS1QFiZlSUq0DyXlPi1oUGJxGZVgYl70hX3bEopBbAEZhoBVbSfKKY4BP8rQ6suPeJKr/iFxP8xPQxfAcA4vnZq2rRaJudT0VXwdmSmBFzfwVlVaQBGp9B+q1k7ZKVAvEaecXEsbcDmRe6yzmF75Ilzj5D5rR4uu95LWiGN16lV2GoQczr3t18U44G9ETcP+EaC5OyIwOF94/KZEec/TxU9Ng7hJnkeQ7kdgKUSGwHRd0aH7+amchxRFxhraTKbRp7xpdJ0a1riST+ERyjUKq402m/Edpr3zyc1jbgadlxIPOyg9sKxy0Wsk/8xp5lxBBA67H+1VnBcV/zXDNnfpm1AIaxsM56A5uenM1CP6pkSl+1Gsp45uQMZQcWD8r3TM2/CZ7vNG8TZ7yg57GMEtMteBlaQDc235rPYjFBpAcS6CXFxMgQPhbziNbRmsdJn4Vxt5LgIY0gn+d0WBLjNpgSeeh2rqKwnheCe9zmVGMLHn42G7WxadZGo81i/ajgQwr3wXBrvgn8RkCx0EAnyWnr1M73Oc1tJ4mXMzUyQ65IIdEGd7noqTinFYMVK+cfkMPkQLye/wBFcWiJGYw7KtR7GUzc7DpuenVX9XhDqDQ+u4b5R1tMblQcM4qKQb7n3bXRHaYA4/37o7FcTe/4y2b3FNpgQIIJdzC0ZKKrDFjixpfUE5zbsj/HJXvAWtge7zvYRqQIJBMC/wBOiqW41twahkHamyw3BvbvHpqtFwZ7IBBd3kz1gACPACUgQbXaYiLxYEb94lZ1787HWOaSDMHpaNRqtJiMRmvAcBto4bdnae6Ss7j202OLSXMlzjBBc0EmdR2hczode5RV6NO1FWK5psc2TYR1BI0PiUT7H0prFx0DT5mAPqhMc+oJntMJkOMVGQOUyGnaLFX/ALP4YNDZGQuE2mDfqSQVWkSss05ShPDUoXmy2dCI4XC1TZVwtU2BEVE8KdzUwtTTAhCkFQp2Vcyp2gOe8KS7lSRgLYZhXNa0GTEwB3J9etYk2ncck6nTbnkwIFuakxNMARIA7l06J9KKri5ljLDUk6lSYdk6aRc79TOyjq0A99rjXvPVEvxfuqZDTlk3cbd0cz0TTwNoKpYaO0YgDkYFxlAG5+qZqx4Y651eeZ5cxFuSKoNcGsJPxc9dNByN78kxlMNztFup79fNZMaKD2lpkU2PaJLQbmJaQ0y7oSS0T39FkeAPDHsAuXOv+3S3it/iafvKNVn8rg0xoBlk9/xf7V53hKOSuydJHjaAPN3oF1cOY0c/LiVlvjKnxxqOwD+UZB9+alovDTm0GXMejWiQOpF+8hDNfm96eeV3/lkn09FLiaR/hv7XMJ8SDK0lEUZGk4B7QUKlEMrsGYyA7e9y48mgxefksx7QexVVjy9svYQHZouSdgJ7k3hlPIC86NZYHQu/DPQOmy1Psx7TNyFlaC21zqTz+V+mt1n/AJeBvKPPa/AHtkXkRtYTJuieF8GqkljpDYmCeye5bzH1aIcHsdIeYFr2bmvzt81U8R4qMsMERv43VKTYdUirw3AqNN5c9+awIEjXr8kTUMsOS19Oma4j1Vd8Jzcg0nxIP1KsaFKQQN/mAD/6p5YYWhz8RLXB1wQ4a3HZ1ad9tZVJxDFOcGmQ9rbX6jMN8zDY6GDl30VnxFmVrv7iOllmzUIJI3kHlY79DHqqSJkwvhVLM7skwLkH4mwIlrhE+ltt1s8AJLZi1u/w2Ko/Z/DANJjX4Rvp+6vKECpA3HhPLvsfJZ8jwy4Iuw1OyprHInOIXnVbNngHDV0tTsySQERC4Api1MhAWNcEwsUhCUIAiypKTKkgCbhrDnl1zqpOKkEgHQaj9VNRdlaSO6VkeKYp76kEkdq0OMkDexXYo2TeS6exrBmBA6mBryCqcXxA59GBoIAcT+tvFTVCHNDCSQ0AuOncCgeKMbDC1rnOtlbeAeZ+5RS0NfTR1cQ4NpOJzOm8coJAE8zA8UUx8tcXC9h5a+Go6qsFaKLSRJbBMXvpAO9z80Vh3l7SAYJZJOwAB08YhZMsia4Me4uMhwIto0BswfIFYzidASXtEAOcW+Hw90HL5LR4xhFMhxjKBrrMmSes5QByCz1KtmDg4EgBluZIvflYeZW/E6MuRAOCMsrNGobHWz4PkVoBhS+hWbFw6W+In6FUvDaBzn+ZziSLgxUa+B3kN/3FbGg0NZVnSY+nyldN2jnSoxXG6uUNY3x++6ENhHGPX76WU+Lbne4ncz5jRMZYQ3XcrK7NetBbKhLhfSY++5J7Mzb/AH9z6JtBsffP79VI90ApWOiEkG3NoHfFvorfhThnyO6Hz39PVZ+kfiI1aD6An6K8eQx7H/hMtJ5fCfKw8lrHKM5YZFx9kAjk/wAbT9IWWZTkx4rXe1PZudwXehZPq1ZnhTJffuPqqI2zS8J0jcEwfl9EUMQM4m36j91ScPxRaXSLD6a/fRW2IaOwTuT8gsGs5OhawbDDMY9gdOy5kBsFS8Oc4NNMnaWlc/1RzIGXTVYTglpDjbL1uFK7/Bu6KtpcfG9kfheNsdaVn0XqG1IY9jgUxzSFYuxbSJUTsS2EpQS9Em/gAF1HYYB5gBT18I1jZkJLjbyh2VKSIyMSVfiGV3FsU9rABlDd3OdHgAs42mc4yXk3dJjwR2Jmp8bQ5o0beZ8VGyQ0EMyAWg3kdCT3LpWETRZvaGAS+G/Eec8538lXYisWdt7pDyMjIyiPzO3jorCmwCHOfYaNBGv8xHyVJxF761WSIY3STBPhyUJWym60WlHG5m9qzJ3s0AchuUdwLFZ87rbtYNmsBABnz8lkcRimvIYA4hpvI7PirrglcAgAhjRE9bO18ZMch1RKFKwjK3RZ8UqtOdgEjsyebjsOcW8Y5LFcQxL2PyNGrgSbmYNh6n05K+4vxFjHgXidfzOOwHSNe5VlagIkzI7XXX0t804YVimrwGcEw4Jk3DGG+uZ7iHHv0jwU/EcblaWTJy9rqXEH5ShuH8SaxhZMG5HMkgX7gPXvVIzFHPDpvfxmw8lq5OjNRVkr9T5d+gCeGRbcrlVsG25B8v8AKcHBo6x9+pUGgnuyhgG749CfoFFjHntD72P6rlZ85ehn0TS7NJd3H78UAQ0idRuD5x/laHDMD6WU7NB/X0t4qiHZGXl+/wC6s+G4sMJnSCP9sH5q4yyZuOCx43hfeYZl+0zsE/1QPLTyWe4QyxJ/IPPQ+MrW0yxzCPwlseEepj5LMYhjqT3s5kkf7pt/5LVu4maVSDcNQBkRrPz/AEReMZGVp/BH6X+91DwphbJfzB6JmMq5s97EuaSOQ+E+BWN5N6DKfEWtJeDoIA6qsZiqjiS4ggnTkhqMDqF2i54kgBDyKKosG0WETMHkpcBVYTBOU9VUtxRO1wbpVgHXul1L7GyGMYxo7UhRO4k1wMLN0XtAgm0Lpc20OKz6fSuyLWhxwtJIJO0Kc8Ve9nacR0VOyiNAUU2ieeyrqvACv9Qd+b0SQX8M7mklQE4rBhhrxM2BM+kqFrC9xe9rzJ0ObKO5osk59CA+oCwu/EJ+Y0HerBwYQIeQItBAzCP8K9GeysxToe0h+VmnuwI9AF2riYBIBcdNvCyCfV95UJMSLWEGPEwn4nFZGggOcZ0AE+miEh9kDYWo9xIcwtubAZZ6kn5o/A1WF0zOQzN4nSBz5eaEw2NL5L2ZBax38P2R2HaAZ2ib29Bom0SmS4lrXvBMEtJOnLU+dvFDVBIMbk36THzn0UVFwL3OaRe0eYzHoAXEIyqBlEbQI00v8h6pJUO7KvG4UF+Yco6D9ohNYzOM0aDN3nT6IlxBDp/FmjyEfMLuQMaG7gGe8k/v5pvQlsrcNXl2U7gkeAaR6z5J4Zc8pMd0/qoKlGHA/lMD1CNNMhrTvBnpzKKEmyB5Ezynz+/koXOJsNxfwKIFMx3EHvI/z6JU2Q2NTp32hKhtg1MOInw9bKWjTcTyuD4iJ++iJbS7Pd9P8IgMNuoB/X1KLHRNgKxY0Am2g6EW9RPoiMfSDwx4159RaD97nkg8NTLo3B08reshSh5YIcYmR47H0T7MSijtevkpuG5tHeZHy9UHRpky9x1bp1AufQKJ9WM8menK4MBH0W5mBw5HoIhAwNlIwSBCWXLYGeoXHuNoNvkiMoy280AgapSv2TEjcKN4e0Entd36Kd4PZ5cwbpj3EGNp13QAqLyRaNNCFK2DrZBvouBlsxz6qek1xaZMckAmOfUawy6fBF4bFMd8BcehkICrhnWObwP0TsPVLSZBtuNEVYdqLbOOqSB/ieq4jqHcL4nxEhwhoc02OgHkhcbh2VC14eWkbAjyABQeKoMZ8RcHTa5JPgEDicU9hb2jJ2I7R748kJEOX0O/iMpIMg6TFv1UgrvEgjN1Fz3wFWsxr82QjMTqJgDrb7sp2vGYOJLSItBI7lVE9iQYVr+2SbbkH0bKIwz3F0PgN5wTbr1XH4pwcA0CDqND+qmqva6GiZJ5opjtD20Wt0tmOpt3nyCke6Gxt8r3Plbz6J1cm2YAZR4Acp+Z8kJqLTPM6nr0CVFWSmlL2mYygA95GnhBTasEjlrH8uoj1QjnhoytM6kk65nECZ8J8FJRf8I6tHc24HoECGOaSOuYEeDiP1UlSpo3b9U9jO0319CfkVFXb2nWuPv5hIZLh7gGLTPz/ZJ4ykZRoT6WH1TsNSMt5b+LZ+gRTh2gNvqJ+sIGQ0hGv3YfWU+i0kwDq2PMmPkp6bc3nPfJd9Sne5gA6EA/tHr5JUwtELCWxkNgR8ocFHVpm2cA894RFOkA4uIuTcbTsUzEs7WczIEcvOCqSFYHVosHbiQbOgeUj71RprSwgCw18dkLScCSWnvFo/yin1ewGMbY3PPRJoE7B2i8ayNF1ok221TXMdbbSDyP6KSmb3MdYsUrLGVGg3Gm6QwrY0lcbU1E3Jty9FOK4HZOvqiwwOJgRCDxfZylrfK6MqkRN43QlbFZDbxsndiaSIGPc4j8McwpffdqAR5Kahimus4W1k7HoiwxhaYAPgi6BKwO38vkkp8rPy+iSXYfUo+Jf9yz+sfRR1v+5/tPzSSVoxlsjwvxv8FLX+PxHzckkqF4WWC+A9wUX43JJKlol7Dan/TPfT+aiGnh9EklBp6BV9+8/JSYf4j/AG/VJJShhNHb73UdX439/wBUkkhhlP6n5BRP+H+4fMrqSEAdQ0b/AG//AGFPH/TZ3fqkkrIBW/T/APSHxXxn+lvyK6kgbAKXx1P6vojsJ+H75rqSUtBAIf8AQKMaHvKSSzRswPE7f1Bdx3xD73SSTEGs+F/gha3wHwSSQhPQJ+LyVlhNfFJJEhxCEkklBR//2Q==', 'artist': 'NA', 'source_url': 'NA', 'error':'NA'}])

df.sql('Felinos', conn, index=False, if_exists='replace')
