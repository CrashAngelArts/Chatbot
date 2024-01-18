from dataclasses import dataclass, field
from uuid import uuid4

def new_id():
	return str(0)

@dataclass
class Categories:
    category_id: str
    category: str
    category_text: str

@dataclass
class Phrases:
    phrase_id: str
    category_id: str
    phrase: str
    dependencies: list = field(default_factory=list)

@dataclass
class Phrases_Reply:
    phrase_id: str
    phrase_reply_id: str


def add_cat(array, category, desc):
 array.append( Categories(category_id=new_id(),category=category,category_text=desc))


def add_phrase(category_id, array = [], phrase = ""):
    array.append(Phrases(phrase_id=new_id(),category_id=category_id,phrase=phrase,dependencies=[]) )

categories = []
negatives = []
positives = []

#phrase_replies = [Phrases_Reply(phrase_id=neg[0].phrase_id,phrase_reply_id=pos[0].phrase_id),]


add_cat(categories, "Exclusões simples (substantivos não especificados", "Substantivos (ou pronomes) vagos que criam confusão e ambiguidade\nDesafios Positivos : Aponte para o especificador ausente:")
add_phrase(categories[0].category_id, negatives, "É hora de você encarar a realidade.")
add_phrase(categories[0].category_id, negatives, "Arranjar uma vida.")
add_phrase(categories[0].category_id, negatives, "Esta situação é impossível")
add_phrase(categories[0].category_id, negatives, "Há certas coisas que você simplesmente não consegue passar pela cabeça.")
add_phrase(categories[0].category_id, negatives, "Não é o que você sabe, é quem você conhece.")
add_phrase(categories[0].category_id, positives, "De quem é a realidade?")
add_phrase(categories[0].category_id, positives, "Que tipo de vida?")
add_phrase(categories[0].category_id, positives, "Qual situação")
add_phrase(categories[0].category_id, positives, "Quais coisas especificamente?")
add_phrase(categories[0].category_id, positives, "O que não é o que quem sabe? Quem precisa saber")

add_cat(categories, "Exclusões simples (adjetivos não especificados)", "Adjetivos cujos significados não são especificados. Adjetivos não especificados são um indicador frequente de interpretação, em vez de observação, e muitas vezes levantam a questão da perda de performativos (veja abaixo).\nExemplos negativos :\na. 'Eu atraio comportamento idiota.' \nb. 'Você precisa usar esse chapéu bobo?' \nc. 'Por que esse olhar presunçoso?' \nDesafios Positivos : Aponte para o especificador ausente:\na. 'Idiota de que maneira?' \nb. 'Bobo na opinião de quem?' \nc. 'Que tipo de aparência é 'presunçosa'?'")
add_phrase(categories[0].category_id, negatives, "Eu atraio comportamento idiota.") 
add_phrase(categories[0].category_id, negatives, "Você precisa usar esse chapéu bobo?") 
add_phrase(categories[0].category_id, negatives, "Por que esse olhar presunçoso?")
add_phrase(categories[0].category_id, positives, "Idiota de que maneira?") 
add_phrase(categories[0].category_id, positives, "Bobo na opinião de quem?") 
add_phrase(categories[0].category_id, positives, "Que tipo de aparência é 'presunçosa'?")

add_cat(categories, "Exclusões simples (relacionamentos não especificados)", "Relações entre termos ou ideias que são assumidos e não especificados.\nExemplos negativos :\na. 'Preciso comprar roupas novas antes de me sentir confiante.' \nb. 'Eu tenho esse problema há muito tempo, então será difícil mudar.' \nc. “Não posso ter um relacionamento até perder peso.” \nDesafios Positivos :\na. 'Existe alguma coisa em que você se sinta confiante que não exija roupas novas?' \nb. 'Qual é a relação entre tempo e facilidade de mudança?' \nc. 'O que conecta especificamente os relacionamentos ao seu peso?'")
add_phrase(categories[0].category_id, negatives, "Preciso comprar roupas novas antes de me sentir confiante.") 
add_phrase(categories[0].category_id, negatives, "Eu tenho esse problema há muito tempo, então será difícil mudar.") 
add_phrase(categories[0].category_id, negatives, "Não posso ter um relacionamento até perder peso.")
add_phrase(categories[0].category_id, positives, "Existe alguma coisa em que você se sinta confiante que não exija roupas novas?") 
add_phrase(categories[0].category_id, positives, "Qual é a relação entre tempo e facilidade de mudança?") 
add_phrase(categories[0].category_id, positives, "O que conecta especificamente os relacionamentos ao seu peso?")

add_cat(categories, "Exclusões comparativas","Frases e sentenças que implicam uma comparação, mas excluem o objeto no qual a comparação se baseia, ou que não especificam a base da comparação. Palavras frequentes: mesmo, muito, mais, menos, maior, menor, maior, mais brilhante, mais inteligente... etc. (do que? como?). Desafios Positivos : Especifique a exclusão"
add_phrase(categories[0].category_id, negatives, "Até você pode entender o que estou prestes a lhe dizer."
add_phrase(categories[0].category_id, negatives, "Se seus gostos fossem melhores, as pessoas gostariam mais de você."
add_phrase(categories[0].category_id, negatives, "Você acha que poderia falar menos e pensar mais?"
add_phrase(categories[0].category_id, positives,"Mesmo? Comparado com quem?"
add_phrase(categories[0].category_id, positives,"Melhor? Do que o quê?"
add_phrase(categories[0].category_id, positives,“Fale menos e pense mais do que quem?”

add_cat(categories, "Índice Referencial Não Especificado","Uma frase que exclui quem está atuando. Usar um assunto geral que não se refira a uma pessoa específica. Palavras frequentes: uma pessoa, alguém, pessoas, eles, um, nós. Além disso, generalizações que se aplicam a classes ou grupos de indivíduos: “Americanos, católicos, judeus, gestores, trabalhadores, homens, mulheres, etc. Desafios Positivos : Especifique a exclusão."
add_phrase(categories[0].category_id, negatives, "Uma pessoa pode ficar realmente farta de você."
add_phrase(categories[0].category_id, negatives, "As pessoas não gostam de você."
add_phrase(categories[0].category_id, negatives, "Não se vai aprender o que não se quer saber, não é?"
add_phrase(categories[0].category_id, negatives, "Uma esposa deveria pelo menos preparar o jantar para um homem."
add_phrase(categories[0].category_id, negatives, "Um corpo deve se perguntar o que está acontecendo nesse seu cérebro!"
add_phrase(categories[0].category_id, positives,"Que pessoa?"
add_phrase(categories[0].category_id, positives,"Que pessoas?"
add_phrase(categories[0].category_id, positives,"Qual deles?"
add_phrase(categories[0].category_id, positives,"Qual esposa deveria preparar o jantar para qual homem?"
add_phrase(categories[0].category_id, positives,"De quem é o corpo?"

add_cat(categories, "Verbos não especificados","Processe palavras que não tenham uma descrição completa e verbos que sejam, em maior ou menor grau, não especificados. Além disso, omitindo o verbo, ou o objeto do verbo, ou ambos. Desafios Positivos : Apontam para especificador ausente."
add_phrase(categories[0].category_id, negatives, "Não me force a ficar com raiva de você novamente."
add_phrase(categories[0].category_id, negatives, "Você nunca expressa seus sentimentos."
add_phrase(categories[0].category_id, negatives, "Eu gostaria que você não falasse assim."
add_phrase(categories[0].category_id, negatives, "Ah, pare de choramingar."
add_phrase(categories[0].category_id, positives,"Forçar você como?"
add_phrase(categories[0].category_id, positives,“Expressar de que maneira?”
add_phrase(categories[0].category_id, positives,"Conversa?"
add_phrase(categories[0].category_id, positives,"Choramingando exatamente como?"

add_cat(categories, "Nominalizações","Um processo (verbo) que foi convertido em uma coisa ou evento (substantivo) . As formas comuns de nominalização incluem adicionar "-ing" ou "-tion" a um verbo para torná-lo um substantivo. JDH: Nominalizações Indutivas de Identidade: adicionar “-er” a um verbo para classificar uma identidade por meio de uma equivalência complexa. "Eu vejo você andando. Portanto, você é um caminhante." O processo é de equivalência complexa: "Vejo você andar e isso significa que você é um caminhante." O falante que não tem consciência desta armadilha linguística pode muitas vezes apenas acreditar que se chegou a um “significado” quando o processo foi convertido numa classe. Desafios Positivos : Converter a nominalização novamente em um processo."
add_phrase(categories[0].category_id, negatives, "Os homens não apreciam os sentimentos ou a intuição."
add_phrase(categories[0].category_id, negatives, "Mulheres como você não têm sucesso."
add_phrase(categories[0].category_id, negatives, "Se você tivesse um novo pensamento de vez em quando, sua compreensão não seria tão trivial."
add_phrase(categories[0].category_id, negatives, "Você tem dificuldade com decisões."
add_phrase(categories[0].category_id, positives,"O que você aprecia nos homens?"
add_phrase(categories[0].category_id, positives,"Temos mais sucesso naquilo que amamos."
add_phrase(categories[0].category_id, positives,"Eu me pergunto se entendi suas intenções."
add_phrase(categories[0].category_id, positives,"Então foi isso que você decidiu."

add_cat(categories, "Operadores modais de necessidade","deve, não deve, tem que"
add_phrase(categories[0].category_id, negatives, "Você tem que agir em conjunto."
add_phrase(categories[0].category_id, negatives, "Tenho que ganhar pelo menos US$ 500 mil por ano."
add_phrase(categories[0].category_id, positives,"O que aconteceria se eu não o fizesse?"
add_phrase(categories[0].category_id, positives,"De acordo com que critérios?"

add_cat(categories, "Operadores modais de possibilidade"," posso, não posso, não posso. Desafios Positivos : Destacar o operador modal::"
add_phrase(categories[0].category_id, negatives, "Você pode me trazer uma cerveja."
add_phrase(categories[0].category_id, negatives, "Eu não aguento mais seu cabelo."
add_phrase(categories[0].category_id, negatives, "Ela poderia ser mais inteligente."
add_phrase(categories[0].category_id, negatives, "Ele não poderia ser mais burro."
add_phrase(categories[0].category_id, negatives, "Eu não consigo entender isso."
add_phrase(categories[0].category_id, positives,"O que aconteceria se eu não fizesse isso?"
add_phrase(categories[0].category_id, positives,"O que aconteceria se você aguentasse meu cabelo?"
add_phrase(categories[0].category_id, positives,"Ela poderia ser mais inteligente se o quê?"
add_phrase(categories[0].category_id, positives,"O que o impede?"
add_phrase(categories[0].category_id, positives,"Não pode? E se você pudesse?"

add_cat(categories, "Operadores modais de julgamento","deveria, não deveria, deveria, (ver também Performativo Perdido). Desafios Positivos : O mesmo que o desafio ao Performativo Perdido"
add_phrase(categories[0].category_id, negatives, "Você deveria ser um cozinheiro melhor."
add_phrase(categories[0].category_id, negatives, "Você não deveria usar essas cores."
add_phrase(categories[0].category_id, positives,"De acordo com quem?"
add_phrase(categories[0].category_id, positives,"De acordo com qual parte de mim?"

add_cat(categories, "Operadores Modais de Contingência","faria, não faria. Desafios Positivos : Destacar operador modal"
add_phrase(categories[0].category_id, negatives, "Certamente você deve ter percebido que eu ficaria com raiva [se você fizesse isso]."
add_phrase(categories[0].category_id, negatives, "Você não pareceria natural em um carro tão caro."
add_phrase(categories[0].category_id, negatives,"Eu faria uma mudança."
add_phrase(categories[0].category_id, positives,"Você faria? Como você prefere ficar?"
add_phrase(categories[0].category_id, positives,"Eu não faria isso? Se o quê?"
add_phrase(categories[0].category_id, positives,"Você faria isso, exceto por quê?"

add_cat(categories, "Pressupostos","Declarações nas quais algum elemento não declarado deve ser assumido (pré-suposto) como verdadeiro para que a afirmação faça sentido (seja verdadeira ou falsa). Isto é, a estrutura superficial das declarações (as palavras específicas e os seus significados) omite ou obscurece a estrutura profunda das declarações (a sua mensagem subjacente ou verdades pressupostas). No Metamodelo, as formas de pressuposição são nomeadas de acordo com a maneira pela qual as sentenças que as contêm as excluem ou obscurecem na estrutura superficial. 29 As formas de pressuposição do metamodelo foram explicadas por Bandler e Grinder em "The Structure of Magic" Apêndice B, 1975. Na coleção de formulários do Metamodelo desta página, apenas uma pressuposição é incluída por razões de brevidade. Clique aqui para ler o artigo completo sobre formulários de pressuposição de metamodelo. 7h. Violação de restrição seletiva Atribuir consciência a um objeto inanimado, a uma abstração, a um modo de comunicação ou a uma criatura ou entidade que não possui esse modo. ("Uma cadeira pode ter sentimentos.") Além disso, negar a percepção consciente em seres conscientes, ou negar um modo de comunicação ou capacidade a uma criatura que possua esse modo. Além disso, excluindo categorias complementares por descrição definida (gênero, raça, religião, etc.). Desafios Positivos : Desafie diretamente ou reformule com a mesma estrutura."
add_phrase(categories[0].category_id, negatives, "Você tem a personalidade de um toco."
add_phrase(categories[0].category_id, negatives, "Seu vestido provavelmente deseja que você fosse mais jovem."
add_phrase(categories[0].category_id, negatives, "Homens causam guerras."
add_phrase(categories[0].category_id, negatives, "As mulheres são manipuladoras."
add_phrase(categories[0].category_id, negatives, "Para o meu papagaio sou apenas 'The Food Lady'."
add_phrase(categories[0].category_id, negatives, "Pela primeira vez, Juno irá mapear toda a atmosfera de Júpiter até uma profundidade de 350 milhas. Os vastos sistemas climáticos de Júpiter podem finalmente revelar os seus segredos."
add_phrase(categories[0].category_id, positives, "Tocos sempre falam bem de você."
add_phrase(categories[0].category_id, positives, "Meu vestido definitivamente deseja que você seja mais inteligente."
add_phrase(categories[0].category_id, positives, "Acreditar que os homens causam guerras provoca uma guerra entre os sexos.”
add_phrase(categories[0].category_id, positives, "Então, toda mulher é sempre manipuladora e nenhum homem é?"
add_phrase(categories[0].category_id, positives, "Então, o que você acha da comida?"
add_phrase(categories[0].category_id, positives, "Os sistemas meteorológicos de Júpiter estão escondendo intencionalmente seus segredos?"

add_cat(categories, "Quantificadores Universais","Palavras que são generalizações absolutas sem índice referencial. Palavras frequentes: sempre, nunca, todos, todos, nenhum , etc. As transformações destacam o quantificador universal e o questionam."
add_phrase(categories[0].category_id, negatives, "Você sempre usa essa camisa."
add_phrase(categories[0].category_id, negatives, "Com você, é sempre alguma coisa."
add_phrase(categories[0].category_id, negatives, "Ela é assim o tempo todo."
add_phrase(categories[0].category_id, negatives, "Ele nunca chega na hora certa e nunca se veste adequadamente."
add_phrase(categories[0].category_id, negatives, "Toda vez que tento, falho."
add_phrase(categories[0].category_id, negatives, "Nenhum dos meus esforços teve sucesso."
add_phrase(categories[0].category_id, positives,"Sempre? Eu nunca uso mais nada?"
add_phrase(categories[0].category_id, positives,"Sempre? Sem exceção?"
add_phrase(categories[0].category_id, positives,"Então ela nunca deixa de ser assim?"
add_phrase(categories[0].category_id, positives,"Nunca? Nem uma vez?"
add_phrase(categories[0].category_id, positives,"Todas as vezes? Sem exceção?"
add_phrase(categories[0].category_id, positives,"Nenhum? Nem mesmo um?"

add_cat(categories, "Causa – Efeito","A implicação ou afirmação direta de que uma coisa causa ou é causada por outra, quando não há suporte lógico bem formado ou evidência demonstrável e sensorial para apoiar uma conexão causal.  Palavras frequentes : faz , porque , se...então , como...então , então , desde então , então ."
add_phrase(categories[0].category_id, negatives, "Olha o que você me fez fazer."
add_phrase(categories[0].category_id, negatives, "Sempre que você aparece, nosso time perde." (cláusula subordinada de pressuposição temporal de causa e efeito: “Nossa equipe perdeu porque você apareceu.”)
add_phrase(categories[0].category_id, negatives, "É sua própria culpa ela ter te deixado porque você não gostou da música dela."
add_phrase(categories[0].category_id, positives,"Como exatamente eu fiz você fazer isso?"
add_phrase(categories[0].category_id, positives,"Então a nossa equipa ganha sempre quando estou ausente?"
add_phrase(categories[0].category_id, positives,"Nenhuma mulher jamais abandonou um homem que gostasse de sua música?"

add_cat(categories, "Causa – Efeito -  Exemplos de diálogos internos")
add_phrase(categories[0].category_id, negatives, "Não sou responsável pelas minhas ações porque meus pais foram abusivos."
add_phrase(categories[0].category_id, negatives, "Se não fosse pela economia, eu estaria bem agora."
add_phrase(categories[0].category_id, negatives, "Eu não liguei, então ele se matou."
add_phrase(categories[0].category_id, positives, "Filhos de pais abusivos se comportam de maneiras diferentes"
add_phrase(categories[0].category_id, positives, "Eu poderia estar bem agora, independentemente da economia"
add_phrase(categories[0].category_id, positives, "Para quem eu não liguei e que não se matou?"

add_cat(categories, "Leitura da mente","10a . Acreditar que se conhece os pensamentos, sentimentos, intenções, significados, motivações ou outros processos internos de outra pessoa - sem base em fundamentos razoáveis ​​e lógicos para interpretação ou observação sensorial direta."
add_phrase(categories[0].category_id, negatives, "Você está apenas tentando me fazer parecer um tolo."
add_phrase(categories[0].category_id, negatives, "Você está me irritando deliberadamente."
add_phrase(categories[0].category_id, negatives, "Lamento aborrecê-lo com minha história."
add_phrase(categories[0].category_id, positives,"Como você sabe o que estou tentando fazer?"
add_phrase(categories[0].category_id, positives,"Tem certeza que conhece minhas intenções?"
add_phrase(categories[0].category_id, positives,"Então você acha que vai me entediar?"

add_cat(categories, "Leitura Mente -  Exemplos de diálogos internos")
add_phrase(categories[0].category_id, negatives, "Eles devem estar pensando como eu pareço tolo."
add_phrase(categories[0].category_id, negatives, "Eu sabia que ela ia dizer isso."
add_phrase(categories[0].category_id, negatives, "Estou entediando ela."
add_phrase(categories[0].category_id, positives, "Eu me pergunto o que eles estão pensando."
add_phrase(categories[0].category_id, positives, "Achei que ela poderia dizer isso."
add_phrase(categories[0].category_id, positives, "Percebo os olhos dela vagando. Eu me pergunto o que é isso."

add_cat(categories, "Leitura da mente, Acreditar que outra pessoa conhece , não conhece ou deveria conhecer os pensamentos, sentimentos, intenções, significados, motivações ou outros processos internos de si mesmo sem comunicação direta.)"
add_phrase(categories[0].category_id, negatives, "Você sabe o que sinto por você."
add_phrase(categories[0].category_id, negatives, "Você sempre soube que eu iria te deixar eventualmente."
add_phrase(categories[0].category_id, negatives, "Você sabe o que estou passando!"
add_phrase(categories[0].category_id, positives,"Então você sabe o que eu sei? Isso é impressionante. Como você faz isso?"
add_phrase(categories[0].category_id, positives,"Quando você acredita que comecei a saber disso sempre?"
add_phrase(categories[0].category_id, positives,"Então é isso que você pensa."

add_cat(categories, "Leitura Mente -  Exemplos de diálogos internos")
add_phrase(categories[0].category_id, negatives, "Todos percebem que não me sinto confiante agora."
add_phrase(categories[0].category_id, negatives, "Ela deveria saber que quero ficar sozinho por um tempo."
add_phrase(categories[0].category_id, negatives, "Quando penso em alguma coisa, ele sempre percebe!"
add_phrase(categories[0].category_id, positives, "Eles podem não perceber como estou me sentindo agora."
add_phrase(categories[0].category_id, positives, "Ela não pode saber que quero ficar sozinho por um tempo."
add_phrase(categories[0].category_id, positives, "Muitas vezes temos um relacionamento muito bom um com o outro."

add_cat(categories, "Leitura da mente, Acreditar que se sabe que outra pessoa não sabeou compreender o que é aparente à sua observação sensorial, o que foi ou está sendo expresso ou explicado, ou quais são as suas capacidades para compreender."
add_phrase(categories[0].category_id, negatives, "Você não entenderia."
add_phrase(categories[0].category_id, negatives, "Eu já te disse."
add_phrase(categories[0].category_id, negatives, "Você não sabe o quanto estou trabalhando."
add_phrase(categories[0].category_id, positives,"Como você sabe disso?"
add_phrase(categories[0].category_id, positives,"Você está certo?"
add_phrase(categories[0].category_id, positives,"Então você acha que eu não sei o quanto você está trabalhando."

add_cat(categories, "Leitura Mente -  Exemplos de diálogos internos")
add_phrase(categories[0].category_id, negatives, "Mesmo se eu contasse a ele, ele não apreciaria."
add_phrase(categories[0].category_id, negatives, "Ela simplesmente não consegue entender, apesar dos meus esforços para me comunicar."
add_phrase(categories[0].category_id, negatives, "Se eu esperar, eventualmente eles descobrirão o que eu quero."
add_phrase(categories[0].category_id, positives,"Se eu contasse a ele, temo que ele não apreciaria."
add_phrase(categories[0].category_id, positives,"Ela parece não entender o que estou tentando comunicar."
add_phrase(categories[0].category_id, positives,"Se eu esperar, eventualmente eles poderão descobrir o que eu quero."

add_cat(categories, "Leitura da mente, (Crystal Ball Gazing) - Acreditar que se conhece um futuro incognoscível para si mesmo ou para os outros. a. Nota: Violações empilhadas de metamodelo são menos acessíveis ao desafio interativo produtivo, pois, se uma violação for contestada, as outras serão tacitamente aceitas como pressuposto. No entanto, desafiar todas as violações acumuladas é complicado numa conversa natural. Modos de resposta mais eficazes serão encontrados no Modelo Hoag (a ser publicado em data futura)."
add_phrase(categories[0].category_id, negatives, "Nunca encontrarei um homem que me ame."
add_phrase(categories[0].category_id, negatives, “Ele sempre será um viciado.”
add_phrase(categories[0].category_id, negatives, "Meu futuro é sombrio e cheio de dor."
add_phrase(categories[0].category_id, positives,"Então você ficará surpreso quando ele aparecer?"
add_phrase(categories[0].category_id, positives,"Como você pode ter certeza?"
add_phrase(categories[0].category_id, positives,"Como você pode saber com tanta antecedência?".

add_cat(categories, "Leitura da mente", "Violações empilhadas de metamodelo com leitura mental incluem reivindicar qualquer um dos tipos de conhecimento acima sobre os processos internos de outra pessoa, além de usar outras violações de metamodelo (declaradas ou implícitas) como evidência (causa-efeito, equivalência complexa, índice referencial ausente, quantificador universal, perda performativo, etc. psicologização de poltrona, como presumir a capacidade de diagnosticar transtornos mentais ou alegar conhecer ou compreender os processos inconscientes de outra pessoa sem conhecimento profissional ou a capacidade de respaldar a afirmação com padrões razoáveis ​​e amplamente aceitos de comportamento e critérios observáveis."
add_phrase(categories[0].category_id, negatives, "Você não sabe o que estou passando! (mas deveria)"

add_cat(categories, "Leitura da mente", "leeitura de mentes + operador modal de julgamento)"
add_phrase(categories[0].category_id, negatives, "Você queimou os vegetais [e isso significa] que você não me ama."

add_cat(categories, "Leitura da mente", "(leitura de mentes + equivalência complexa)"
add_phrase(categories[0].category_id, negatives, "Você não entenderia porque os homens nunca entendem." 

add_cat(categories, "(leitura da mente + índice referencial ausente/violação de restrição seletiva, causa-efeito)"
add_phrase(categories[0].category_id, negatives, "Se você não fosse tão neurótico, faria o que eu digo."

add_cat(categories, "Leitura da mente", "(adjetivo caracterológico, causa-efeito, pressuposto)"
add_phrase(categories[0].category_id, negatives, "Você sempre esquece onde colocou as chaves do carro. Obviamente você está ficando senil." 

add_cat(categories, "Leitura da mente", "(quantificador universal, equivalência complexa, palavra estática 'senil')"

add_cat(categories, "Equivalência Complexa", "Declarações onde situações complexas , ideias, objetos ou seus significados são equiparados como sinônimos. Palavras frequentes [que são frequentemente omitidas da estrutura superficial da frase]: isso significa, isso significa apenas, deve ser isso, [retórica] o que mais poderia significar?"
add_phrase(categories[0].category_id, negatives, "O chefe está com a porta fechada. Ele está planejando me demitir."
add_phrase(categories[0].category_id, negatives, "Você não está comendo vegetais. Qual é o problema? Você não gosta da minha comida?"
add_phrase(categories[0].category_id, negatives, "Você me comprou flores brancas em vez de vermelhas. Você não me ama como antes."
add_phrase(categories[0].category_id, positives,"Você quer dizer que toda vez que seu chefe fecha a porta, alguém é demitido?"
add_phrase(categories[0].category_id, positives,"Se eu gostasse da sua comida, teria que comer meus vegetais?"
add_phrase(categories[0].category_id, positives,"Então apenas flores vermelhas significam que eu te amo?"

add_cat(categories, "Equivalência Complexa -  Exemplos de diálogos internos")
add_phrase(categories[0].category_id, negatives, "Não sei o que fazer. Devo ser muito estúpido."
add_phrase(categories[0].category_id, negatives, "Estou ficando frustrado. Não posso fazer isso."
add_phrase(categories[0].category_id, negatives, "Eles estão conseguindo e eu não. Simplesmente não tenho o que é preciso."
add_phrase(categories[0].category_id, positives, "Não sei o que fazer. De que recursos preciso para ter uma ideia melhor?"
add_phrase(categories[0].category_id, positives, "Estou ficando frustrado. Talvez eu faça uma pausa e veja se há uma abordagem melhor."
add_phrase(categories[0].category_id, positives,  "Eles estão tendo sucesso e eu não. O que especificamente eles estão fazendo de diferente?"

add_cat(categories, "Performativo Perdido","Julgamentos de valor feitos sem especificar quem está fazendo o julgamento (por exemplo, o executor do julgamento é excluído da declaração)."
add_phrase(categories[0].category_id, negatives, "É bom que sua cabeça esteja presa (ou você esqueceria)."
add_phrase(categories[0].category_id, negatives, "Você tem péssimo gosto para roupas. Isso precisava ser dito."
add_phrase(categories[0].category_id, negatives, "Suas idéias são estúpidas."
add_phrase(categories[0].category_id, positives,"De acordo com quem?"
add_phrase(categories[0].category_id, positives,"Quem precisava dizer isso?"
add_phrase(categories[0].category_id, positives,"Quem disse?"

add_cat(categories, "Performativo Perdido -  Exemplos de diálogos internos")
add_phrase(categories[0].category_id, negatives, "Não sou bom em relacionamentos."
add_phrase(categories[0].category_id, negatives, "Eu aprendo devagar."
add_phrase(categories[0].category_id, negatives, "Eu sou um boneco de computador."
add_phrase(categories[0].category_id, negatives, "As condições em Júpiter são tão turbulentas que as tempestades deveriam explodir."
add_phrase(categories[0].category_id, positives, "Às vezes acho que não sou bom em relacionamentos."
add_phrase(categories[0].category_id, positives, "Percebo que, em comparação com Jim e Kim, sou mais rápido em aprender algumas coisas e mais lento em outras."
add_phrase(categories[0].category_id, positives, "Trabalhar com computadores não é atualmente uma das minhas principais habilidades."
add_phrase(categories[0].category_id, positives, "'Deveria'? De acordo com quem? Ou por qual modelo específico? É possível que as tempestades NÃO se destruam no contexto de um modelo mais amplo que ainda não entendemos?"

add_cat(categories, "Ou/ou","Afirmações ou perguntas que chamam a atenção para uma consequência que pressupõe outra coisa. Cria o que Erickson chamou de “uma ilusão de escolha” e direciona a atenção para considerar apenas as duas possibilidades mencionadas. Desafios Positivos : Superar a limitação nas escolhas."
add_phrase(categories[0].category_id, negatives, "Você está fazendo isso de propósito ou não pode evitar?"
add_phrase(categories[0].category_id, negatives, "Você é estúpido ou apenas ingênuo."
add_phrase(categories[0].category_id, negatives, "Ou ganhamos ou perdemos."
add_phrase(categories[0].category_id, positives,"Essas são minhas únicas duas escolhas?"
add_phrase(categories[0].category_id, positives,"Essas são as únicas duas opções que você consegue pensar?"
add_phrase(categories[0].category_id, positives,"Poderíamos ganhar em um sentido e perder em outro? O que seria verdade se não fizéssemos nenhuma das duas coisas?"

add_cat(categories, "Termos acima/subdefinidos","Termos que se baseiam em definições puramente abstratas que não fazem referência a nada nem a ninguém específico. Tais termos baseiam-se em múltiplos níveis de indireção e tendem a produzir transe (positivo ou negativo). Eles são superdefinidos quando tratamos as palavras como “reais” em si mesmas, quando na verdade são abstrações, e são subdefinidos no sentido de que não usam fatos e detalhes específicos suficientes que se estendam claramente aos referentes reais que consideramos. podemos apontar ou perceber com nossos sentidos."
add_phrase(categories[0].category_id, negatives, “Casei-me com ele porque pensei que ele seria um bom marido .”
add_phrase(categories[0].category_id, negatives, “O crime é causado por problemas de socialização .”
add_phrase(categories[0].category_id, negatives, “Fico impaciente porque não estou sendo produtivo .”
add_phrase(categories[0].category_id, positives,“Se ele se tornasse um bom marido, o que especificamente seria diferente?”
add_phrase(categories[0].category_id, positives,“Que parte da socialização causa quais crimes específicos?”
add_phrase(categories[0].category_id, positives,“O que você quer produzir?”

add_cat(categories, "Divisões Verbais Delirantes (Elementalismo)","Usar a linguagem para compartimentar e dicotomizar elementos de um todo, de modo que pensemos e falemos sobre eles como se realmente existissem separados do todo. Mapas criados com elementalismo não representam o território com precisão e nos impedem de pensar de forma sistêmica. As divisões verbais delirantes comuns incluem: 'mente' e 'corpo', 'espaço' e 'tempo', 'pensamentos' e 'emoções'."
add_phrase(categories[0].category_id, negatives, “Minha mente quer uma coisa, mas meu corpo quer outra.”
add_phrase(categories[0].category_id, negatives, “Racionalmente, sei que não é verdade, mas minhas emoções ainda acreditam nisso.”
add_phrase(categories[0].category_id, negatives, “Parte de mim quer ficar e parte de mim quer ir embora.”
add_phrase(categories[0].category_id, positives,“Sua mente realmente está sozinha?”, Em que contexto sua mente ocorre?, Como seria se o seu corpo-mente quisesse alguma coisa?"
add_phrase(categories[0].category_id, positives,“Se seus pensamentos e emoções se fundissem em uma atitude, qual seria?”
add_phrase(categories[0].category_id, positives,“Quem você será quando essas partes se fundirem em uma só?”

add_cat(categories, "Multiordinalidade (um tipo de nominalização)","Generalizar excessivamente o significado das palavras a ponto de uma palavra ter uma multiplicidade de significados e poder ser aplicada, ad infinitum , a si mesma. Por exemplo, “Tenho um pensamento sobre esse pensamento (e um pensamento sobre esse pensamento sobre esse pensamento)”, etc. Excluído em termos multiordinais está o nível ou dimensão de abstração usada na generalização. Exemplos de palavras incluem “humanidade, estar apaixonado, casamento, trabalho, pensamento, educação, ética, religião, sanidade, insanidade, objeto”, etc. Esses termos são estágios de processos infinitamente valorizados com um conteúdo mutável e ambíguo."
add_phrase(categories[0].category_id, negatives, “Estou tendodúvidassobre nosso relacionamento.”
add_phrase(categories[0].category_id, negatives, “Estouapaixonadopor estarapaixonado.”
add_phrase(categories[0].category_id, negatives, “Isto não é umcasamento.”
add_phrase(categories[0].category_id, negatives, “Temo que usarei o maujulgamentonovamente.”
add_phrase(categories[0].category_id, negatives, “Meu objetivo é serfelizo tempo todo.”
add_phrase(categories[0].category_id, positives,“Que pensamentos você está tendo?”
add_phrase(categories[0].category_id, positives,“De que tipo de amor você está falando?”
add_phrase(categories[0].category_id, positives,“Se isso fosse um casamento, o que seria diferente?”
add_phrase(categories[0].category_id, positives,“Quando você pode determinar que um julgamento será ruim?”
add_phrase(categories[0].category_id, positives,“Se você quebrar a perna, quer ficar feliz com isso?”

add_cat(categories, "Palavras estáticas (um tipo de nominalização)","Um significado fixo ou rígido aplicado a um termo multiordinal . Expressões estáticas soam como pronunciamentos do céu, feitos como se por uma divindade onisciente ou por um legislador inacessível, ou proferidos com uma atitude de  Todo mundo sabe disso... Expressões estáticas mapeiam a realidade em termos e frases absolutistas e dogmáticas, assumidas (ou pretendidas) como verdadeiras sem contestação."
add_phrase(categories[0].category_id, negatives, “É assim quea vidaé.”
add_phrase(categories[0].category_id, negatives, “Crianças são umador.”
add_phrase(categories[0].category_id, negatives, “Você tem que estarjuntopara ficar junto.”
add_phrase(categories[0].category_id, negatives, “Ésolitáriono topo.”
add_phrase(categories[0].category_id, negatives, “Dinheiro não pode comprarfelicidade.”
add_phrase(categories[0].category_id, positives,"Vida? O que você quer dizer? Toda a vida? Qual parte da vida? Para quem? Quando?"
add_phrase(categories[0].category_id, positives,“Quais crianças são um saco quando fazem o quê?”
add_phrase(categories[0].category_id, positives,“Se eu estivesse junto, como eu saberia disso?”
add_phrase(categories[0].category_id, positives,“Isso é sempre verdade?”
add_phrase(categories[0].category_id, positives,“De que tipo de felicidade você está falando?”

add_cat(categories, "Pseudopalavras (um tipo de nominalização)","Mapas linguísticos que não fazem referência a nada na mente (incluindo a lógica abstrata) ou no mundo externo. Podem ser substantivos, adjetivos, verbos, advérbios, expressões, etc. São nomes de coisas que não existem ou ficções baseadas em teorias falsas ou ociosas. Como tal, eles podem depender do contexto. Ou seja, 'unicórnio' não faz referência a nada no mundo externo, mas faz referência a algo na mitologia. Palavras de exemplo: calor, espaço, infinito, propriedade, horrível, horrível."
add_phrase(categories[0].category_id, negatives, “Éterrívelestar sozinho.”
add_phrase(categories[0].category_id, negatives, “Aviolência da verdademe oprime.”
add_phrase(categories[0].category_id, negatives, “Os cientistas podem ter encontrado olimite do universo.”
add_phrase(categories[0].category_id, negatives, “Não podemos terminar de construir sua casa. Ficamos semcentímetros.”
add_phrase(categories[0].category_id, negatives, “Antes do início do tempo, não havia nada.”
add_phrase(categories[0].category_id, negatives, “Tenho a sensação de que tenhofalhas.”
add_phrase(categories[0].category_id, negatives, “Não consigo recuperar minhamotivação.”
add_phrase(categories[0].category_id, positives,“O que você não gosta nisso?”
add_phrase(categories[0].category_id, positives,“Se eu pudesse experimentar a violência da verdade, o que veria, ouviria ou sentiria?”
add_phrase(categories[0].category_id, positives,“Se o universo é o todo de tudo o que existe fisicamente, a sua 'borda' forma a fronteira entre ele e o que mais?”
add_phrase(categories[0].category_id, positives,“Onde você conseguiu os centímetros que já usou?”
add_phrase(categories[0].category_id, positives,“Você está se referindo a um tempo antes do início dos tempos?”
add_phrase(categories[0].category_id, positives,“Falha em vez de perfeita? Por favor, mostre-me a perfeição.
add_phrase(categories[0].category_id, positives,“Talvez eu possa ajudá-lo a encontrá-lo. Você pode me mostrar uma foto disso?

add_cat(categories, "Identificação (um tipo de nominalização)","A raiz da palavra 'identidade' é 'idem', que significa “o mesmo”. Não há duas coisas exatamente iguais em todos os aspectos, portanto não há duas coisas que possam ser idênticas. Nenhuma coisa é igual de momento a momento. Portanto, a identificação é abstrata, resultante da eliminação de distinções. Palavras de exemplo: é, sou, são, um, era, eram, ser, sendo, sido, como, etc.)"
add_phrase(categories[0].category_id, negatives, “Eusouum perdedor.”
add_phrase(categories[0].category_id, negatives, “Vocêexigemuita manutenção.”
add_phrase(categories[0].category_id, negatives, “Este carroétão 'eu'.”
add_phrase(categories[0].category_id, negatives, “souo tipo de pessoa que consegue ter sucesso.”
add_phrase(categories[0].category_id, negatives, “Eu não gosto de quem eusou.”
add_phrase(categories[0].category_id, positives,“O que, especificamente, você perdeu?”
add_phrase(categories[0].category_id, positives,"Como você está me mantendo?"
add_phrase(categories[0].category_id, positives,“Como é você?”
add_phrase(categories[0].category_id, positives,“Como é útil identificar-se com um tipo?”
add_phrase(categories[0].category_id, positives,“Como você é diferente do ‘você’ de quem você não gosta?”

add_cat(categories, "Emocionalizando","Usar nossas emoções para coletar e processar informações : “Eu sinto, então deve ser verdade”. A emocionalização confunde experiências geradas internamente e geradas externamente, de modo que, em vez de simplesmente vivenciar uma emoção, a usamos como evidência de uma situação externa negativa correspondente. As emoções surgem em resposta a diferenças ou semelhanças entre os nossos mapas e os territórios que representam."
add_phrase(categories[0].category_id, negatives, “Fui demitido hoje.” [Nota: Isto foi afirmado por um cliente que não foi demitido. Sua explicação para a discrepância entre o que realmente aconteceu e sua declaração foi: "Bem, pareciaqueeu tinha sido demitido."]
add_phrase(categories[0].category_id, negatives, “O mundo é um lugar sem esperança.”
add_phrase(categories[0].category_id, negatives, “Ele me ama, eu posso dizer.”
add_phrase(categories[0].category_id, negatives, “Que vida triste é essa.”
add_phrase(categories[0].category_id, positives,“Que palavras seu chefe usou para demiti-lo?”
add_phrase(categories[0].category_id, positives,“Então você está se sentindo desesperado?”
add_phrase(categories[0].category_id, positives,"Como você sabe?"
add_phrase(categories[0].category_id, positives,“O que faz você se sentir triste?”

add_cat(categories, "Personalização","Interpretar eventos, especialmente as palavras ou ações de outros, como sendo especificamente direcionados a nós e/ou como um ataque a nós . Este processo conecta de forma imprecisa os eventos externos à nossa autoimagem, opinião própria e autodefinição e, em última análise, renuncia à capacidade de resposta às nossas próprias escolhas e ações. Palavras de exemplo: eu, eu, meu."
add_phrase(categories[0].category_id, negatives, “Estou sob constante ataque da sociedade, das finanças e dos relacionamentos.”
add_phrase(categories[0].category_id, negatives, “Eles fazem hambúrgueres grandes demais, por desrespeito à minha saúde.”
add_phrase(categories[0].category_id, negatives, “Ela não me quer aqui. Ela perguntou quanto tempo eu ficaria.
add_phrase(categories[0].category_id, negatives, “Ele me abandonou. Em todas as temporadas de futebol ele ficava grudado na TV.”
add_phrase(categories[0].category_id, positives,“Alguém está atacando você agora? Você pode apontá-los para mim?
add_phrase(categories[0].category_id, positives,“Se eles fazem um hambúrguer, o que você precisa fazer para engordar com ele?”
add_phrase(categories[0].category_id, positives,“Como você sabe que ela não estava apenas planejando seu tempo?”
add_phrase(categories[0].category_id, positives,“Como você sabe quando levar isso para o lado pessoal?”

add_cat(categories, "Metáforas","Compreender e experimentar um tipo de coisa em termos de outro . A metáfora é diferente da comparação. Metáfora: “Meu amor é uma rosa”. Símile: “Meu amor é como uma rosa”. As metáforas são uma característica importante da linguagem, mas podem criar estados negativos quando consideramos os seus significados e o facto de serem metáforas como garantidos sem exame. Assim como a identificação, eles eliminam as diferenças. Exemplos de palavras-chave: é, são, eram, ser, etc."
add_phrase(categories[0].category_id, negatives, “Ela é uma mercadoria danificada.”
add_phrase(categories[0].category_id, negatives, “Estamos nadando em um mar de toxinas criadas pelo homem.”
add_phrase(categories[0].category_id, negatives, "Tempo é dinheiro."
add_phrase(categories[0].category_id, negatives, “Ele é um pé no saco.”
add_phrase(categories[0].category_id, negatives, "A vida é uma droga."
add_phrase(categories[0].category_id, positives,"Como ela foi ferida?"
add_phrase(categories[0].category_id, positives,“O ‘mar’ é semelhante ao que na sua experiência?”
add_phrase(categories[0].category_id, positives,“O que mais é o tempo?”
add_phrase(categories[0].category_id, positives,“O que ele faz, especificamente?”
add_phrase(categories[0].category_id, positives,“Isso é tudo o que a vida faz?”

add_cat(categories, "Modelo Milton, Perguntas sobre tags", "Uma pergunta adicionada no final de uma afirmação, que muda o foco da atenção do ouvinte para responder à pergunta-chave, longe da afirmação anterior. As perguntas sobre tags às vezes são acompanhadas por uma mudança temporal. Desafios Positivos : Retornar o foco para a declaração."
add_phrase(categories[0].category_id, negatives, "Você sempre consegue virar o jogo contra mim, não é?"
add_phrase(categories[0].category_id, negatives, "Você realmente conseguiu desta vez, não foi?"
add_phrase(categories[0].category_id, negatives, "Você nunca aprenderá, não é?"
add_phrase(categories[0].category_id, positives,"É nisso que você acredita?"
add_phrase(categories[0].category_id, positives,"Feito o que em oposição a que horas?"
add_phrase(categories[0].category_id, positives,"Essa é a lição de hoje?"

add_cat(categories, "Milton, Postulados Conversacionais", "Uma pergunta do tipo “sim ou não” à qual o ouvinte responde fazendo ativamente o que está implícito. O exemplo mais simples é: “Você pode me dizer que horas são?” (A maioria das pessoas olha para o relógio e diz a hora, respondendo com comportamento em vez de responder à pergunta real.)"
add_phrase(categories[0].category_id, negatives, "Por favor, pare de me dizer isso?"
add_phrase(categories[0].category_id, negatives, "Você se importaria de não olhar para mim desse jeito?"
add_phrase(categories[0].category_id, negatives, "Você pode mover sua gordura um pouco?"
add_phrase(categories[0].category_id, positives,"Nenhuma ação. Uma simples resposta “sim” ou “não”, ou nenhuma resposta se as pressuposições estiverem incorporadas – sem fazer o que está implícito ."
add_phrase(categories[0].category_id, positives,"Nenhuma ação. Uma simples resposta “sim” ou “não”, ou nenhuma resposta se as pressuposições estiverem incorporadas – sem fazer o que está implícito ."
add_phrase(categories[0].category_id, positives,"Nenhuma ação. Uma simples resposta “sim” ou “não”, ou nenhuma resposta se as pressuposições estiverem incorporadas – sem fazer o que está implícito ."

add_cat(categories, "Milton, Ambiguidadee Sintática", "Onde a função de uma palavra não pode ser conhecida rapidamente a partir do contexto imediato."
add_phrase(categories[0].category_id, negatives, "Os Smiths estão visitando parentes."
add_phrase(categories[0].category_id, negatives, "Frank é um consultor de treinamento."
add_phrase(categories[0].category_id, negatives, "Os camponeses estão se revoltando."

add_cat(categories, "Milton, Ambigüidade de escopo", "Onde o escopo do contexto linguístico não pode ser determinado. Usar um modificador em um contexto linguístico onde não está claro a qual(is) outra(s) parte(s) da frase o modificador se refere."
add_phrase(categories[0].category_id, negatives, "Notei seus hábitos bagunçados e suas toalhas no cabide."
add_phrase(categories[0].category_id, negatives, "Falando com você como uma pessoa inteligente, a linguagem nem sempre é clara." 
add_phrase(categories[0].category_id, negatives, "Há um tempo e um lugar para tudo e este é um deles."
add_phrase(categories[0].category_id, positives, "(As toalhas estão bagunçadas? Os hábitos estão no cabide?)"
add_phrase(categories[0].category_id, positives, "(O falante é uma pessoa inteligente ou o ouvinte é uma pessoa inteligente?)"
add_phrase(categories[0].category_id, positives, "(Isso é uma hora ou um lugar?)"




#  pressupositions 
phrases = []
pressupositions = []
add_cat(categories, "XXX", "XX"
add_phrase(categories[0].category_id, phrases, ""
add_phrase(categories[0].category_id, pressupositions, ""

add_cat(categories, "Pressupostos  Simples","Pressupõe-se a simples existência de algo, alguém, ou algum tipo ou função particular de algo ou alguém."
add_cat(categories, " Nomes Próprios","Quando um nome próprio é usado, pressupõe-se que a pessoa a quem ele pertence existe."
add_phrase(categories[0].category_id, phrases, " O Sr. Bonito deixou uma mensagem para você."
add_phrase(categories[0].category_id, pressupositions, "Existe alguém chamado, ou que poderia ser chamado, Sr. Bonito."


add_cat(categories, "Pronomes","Quando um pronome é usado, ele pressupõe a existência de alguém a quem se refere."
add_phrase(categories[0].category_id, phrases, "Eu o vi sair."
add_phrase(categories[0].category_id, pressupositions, "Existe algum homem."
add_phrase(categories[0].category_id, phrases, " Penso , logo existo ."  (Descartes) 
add_phrase(categories[0].category_id, pressupositions, "Existe um 'eu' para pensar."

add_cat(categories, "Descrições Definidas","Referir-se a alguém ou alguma coisa em termos de uma definição de papel, categoria ou outra característica pressupõe a existência desse “alguém” ou “algo” naquele papel ou categoria à qual a definição se aplica. Quando usada metaforicamente, esta forma de pressuposto muitas vezes tem a estrutura superficial de uma metáfora caracterológica."
add_phrase(categories[0].category_id, phrases, "Por que deveríamos assistir a um anúncio antes de um filme que acabamos de pagar para ver? Andy Rooney acha que deveria haver uma lei que obrigasse os cinemas a dizer exatamente a que horas o show - e não o comercial - começa."   -  (www.cbsnews.com, 16/08/04)
add_phrase(categories[0].category_id, pressupositions, "Haverá publicidade."
add_phrase(categories[0].category_id, phrases, "Certa vez perguntei ao meu sobrinho de cinco anos: 'Quem quebrou a cerca?' (Eu o vi fazer isso.) Ele respondeu: 'Os assassinos.'  Quem poderia discutir?"  (Stephanie Ericsson, "The Ways We Lie", Companion into the Dawn: Inner Dialogues on Loving, 1994)
add_phrase(categories[0].category_id, pressupositions, "Pressuposto: Existem assassinos (plausivelmente próximos)"
add_phrase(categories[0].category_id, phrases,"Qual é o seu problema ?"
add_phrase(categories[0].category_id, pressupositions, "Pressuposto: Você tem um problema."
add_phrase(categories[0].category_id, phrases,"Uh-oh, aí vem o elefante ."
add_phrase(categories[0].category_id, pressupositions, " Pressuposto: Existe alguém ou algo descritível como “o elefante”."
add_phrase(categories[0].category_id, phrases,"Você não é inteligente o suficiente para resolver o quebra-cabeça ."
add_phrase(categories[0].category_id, pressupositions, " Existe um quebra-cabeça."
add_phrase(categories[0].category_id, pressupositions, " O quebra-cabeça pode ser resolvido."
add_phrase(categories[0].category_id, pressupositions, " É preciso inteligência para descobrir o quebra-cabeça."
add_phrase(categories[0].category_id, pressupositions, " A inteligência é uma qualidade comparativa."
add_phrase(categories[0].category_id, pressupositions, " O palestrante sabe o quão inteligente você é."

add_cat(categories, "Frases nominais genéricas","Argumentos substantivos que representam uma classe inteira."
add_phrase(categories[0].category_id, phrases," Os meninos da mamãe têm que sentar no banco de trás"
add_phrase(categories[0].category_id, pressupositions, " Existem pessoas cuja identidade pode ser descrita como “meninos da mamãe”."

add_cat(categories, "Alguns quantificadores","todos, cada um, todos, alguns, muitos, poucos, nenhum"
add_phrase(categories[0].category_id, phrases," Poucas filhinhas do papai crescem para serem felizes."
add_phrase(categories[0].category_id, pressupositions, " Existem pessoas cuja identidade pode ser descrita como “garotas do papai”."
add_phrase(categories[0].category_id, phrases," Nenhuma das melhores pessoas gostaria de você."
add_phrase(categories[0].category_id, pressupositions, " Existem pessoas melhores."

add_cat(categories, "Pressupostos Complexos","Casos em que se pressupõe mais do que a simples existência de um elemento."
add_cat(categories, add_cat(categories, "Cláusulas relativas","Argumentos de substantivos complexos, com um substantivo seguido por uma frase começando com: quem, qual, com ou aquilo (frequentemente omitido)."
add_phrase(categories[0].category_id, phrases,"A jaqueta feia que  você continua usando me deixa doente."
add_phrase(categories[0].category_id, pressupositions, " você continua usando uma jaqueta feia."
add_phrase(categories[0].category_id, phrases,"As pessoas que dizem que você não está fazendo um bom trabalho não sabem do que estão falando."
add_phrase(categories[0].category_id, pressupositions, " Algumas pessoas estão dizendo que você não está fazendo um bom trabalho."
add_phrase(categories[0].category_id, phrases,"Claro, sou apenas um homem e esta é apenas a minha opinião. Outros com menos experiência são livres para pensar de outra forma.” – Mark Twain"
add_phrase(categories[0].category_id, pressupositions, " Quem pensa o contrário tem menos experiência."
add_phrase(categories[0].category_id, phrases,"São essas as pessoas que você quer que falem com seu Deus por você?” (Pregador no filme de 1997, "Contato")
add_phrase(categories[0].category_id, pressupositions, " Você quer alguém falando com o seu Deus por você.  (Veja também Metamodelo "Ou/Ou" – Observe que responder 'sim' ou 'não' à pergunta valida a pressuposição.)"
add_phrase(categories[0].category_id, phrases,"Sua comida simples , que é boa o suficiente para nós, não servirá para minha família quando eles vierem nos visitar."
add_phrase(categories[0].category_id, pressupositions, " Sua culinária é simples."

add_cat(categories, " Cláusulas subordinadas de tempo","Cláusulas identificadas pelas palavras-chave: antes, depois, durante, como, desde, atrás, antes, quando, enquanto."
add_phrase(categories[0].category_id, phrases,"Se alguém ouvisse você durante um de seus episódios de choro, saberia o quão insuportável você é."
add_phrase(categories[0].category_id, pressupositions, "você tem episódios de choro."
add_phrase(categories[0].category_id, phrases,"Ainda podemos chegar lá a tempo depois que você levar nossas malas para o check-in, se você se apressar."
add_phrase(categories[0].category_id, pressupositions, " Você levará nossas malas para o check-in."
add_phrase(categories[0].category_id, phrases," Quando você for mais velho, você entenderá o que estou dizendo."
add_phrase(categories[0].category_id, pressupositions, " Você não entende agora."
add_phrase(categories[0].category_id, pressupositions, " Você não tem idade suficiente para entender."
add_phrase(categories[0].category_id, pressupositions, " Ser mais velho lhe permitirá compreender."
add_phrase(categories[0].category_id, phrases," Quando acontecer, acontecerá sem qualquer aviso."
add_phrase(categories[0].category_id, pressupositions, " Isso vai acontecer."
add_phrase(categories[0].category_id, phrases," Antes da nossa conversa de ontem à noite, as coisas estavam bem."
add_phrase(categories[0].category_id, pressupositions, "Tivemos “uma conversinha” ontem à noite. (Também uma descrição definitiva : "conversinha", por exemplo, o que tivemos ontem à noite foi uma conversinha . - Este exemplo é tirado de um evento da vida real em que o orador, em uma raiva descontrolada, ameaçou fisicamente violência contra uma pessoa inocente e, no dia seguinte, descreveu suas ameaças enfurecidas como "uma conversa fiada".)
add_phrase(categories[0].category_id, phrases,"Eu só fico bravo com você depois que você faz algo estúpido."
add_phrase(categories[0].category_id, pressupositions, "Você faz coisas estúpidas."
add_phrase(categories[0].category_id, phrases,"“Os investidores estão colocando seu dinheiro de volta no trabalho.” - (anúncio de TV TdAmeriTrade.com, CBS, 24/01/2010, playoff de futebol da AFC, Colts vs Jets)"
add_phrase(categories[0].category_id, pressupositions, Os investidores pararam de colocar seu dinheiro para trabalhar."

add_cat(categories, " Cláusulas subordinadas de localização","Cláusulas identificadas pela palavra-chave: onde. (Nota: a caracterização, “ louca ”, está na estrutura superficial , não na estrutura profunda . Debater se a ideia era maluca ou não aceita o pressuposto de que a ideia não era nossa.)"
add_phrase(categories[0].category_id, phrases," De onde você tirou uma ideia maluca dessas?"
add_phrase(categories[0].category_id, pressupositions, " você tirou a ideia de algum lugar - além de você mesmo."

add_cat(categories, " Frases de fenda", "Frases que começam com "It [era/é]..." argumento substantivo."
add_phrase(categories[0].category_id, phrases," É a sua presunção que me irrita."
add_phrase(categories[0].category_id, pressupositions, " Algo me irrita. (Também pressupõe que o falante esteja em uma posição superior ou objetiva o suficiente para caracterizar absolutamente a 'presunção' como um atributo de quem você é .)"

add_cat(categories, " Frases Pseudo-Cleft","Identificadas pela forma, O que [frase] é [frase]."
add_phrase(categories[0].category_id, phrases," O que ele espera fazer é reparar."
add_phrase(categories[0].category_id, pressupositions, " Ele espera fazer alguma coisa."
add_phrase(categories[0].category_id, phrases," O que sua irritação intencional está fazendo está arruinando nosso relacionamento."
add_phrase(categories[0].category_id, pressupositions, " Você está incomodando intencionalmente."
add_phrase(categories[0].category_id, phrases,"Acho que o que você está tentando dizer é : 'Cale a boca'."
add_phrase(categories[0].category_id, pressupositions, " Você está tentando, sem sucesso, dizer algo."

add_cat(categories, " Frases Tônicas (Estresse Vocal)",""
add_phrase(categories[0].category_id, phrases,"Se você estivesse incomodando SEU CHEFE, você seria demitido."
add_phrase(categories[0].category_id, pressupositions, " Você incomodou alguém."

add_cat(categories, " Frases Tônicas | (Combinado com Frase Cleft)",""
add_phrase(categories[0].category_id, phrases,"Se era SEU CHEFE que você estava incomodando, você será demitido."
add_phrase(categories[0].category_id, pressupositions, " Você estava incomodando alguém."

add_phrase(categories[0].category_id, phrases,"Então foi JIMMY quem mandou você!"
add_phrase(categories[0].category_id, pressupositions, " Você foi enviado."

add_cat(categories, " Uso de adjetivos complexos",": novo, antigo, antigo, presente, anterior, futuro"
add_phrase(categories[0].category_id, phrases,"Seus futuros maridos serão, sem dúvida, mais satisfatórios."
add_phrase(categories[0].category_id, pressupositions, " Seu casamento atual não durará e você se casará novamente mais de uma vez."
add_phrase(categories[0].category_id, phrases,"Ele não está sendo estúpido no momento ."
add_phrase(categories[0].category_id, pressupositions, " Ele foi ou será estúpido."

add_cat(categories, " Uso de números ordinais",": primeiro, segundo, uma vez, terceiro, próximo, outro, último"
add_phrase(categories[0].category_id, phrases,"Da próxima vez que você parecer feio deliberadamente, ficarei em casa."
add_phrase(categories[0].category_id, pressupositions, " Você parece feio deliberadamente agora, ou já pareceu feio deliberadamente no passado."
add_phrase(categories[0].category_id, phrases,"Essa é a última vez que vou aguentar isso!"
add_phrase(categories[0].category_id, pressupositions, "aguentei algo diversas vezes."
add_phrase(categories[0].category_id, phrases, "Naturalmente, posso estar errado. Já aconteceu uma vez ."
add_phrase(categories[0].category_id, pressupositions, " só errei uma vez."

add_cat(categories, " Uso comparativo",": -er, mais, menos"
add_phrase(categories[0].category_id, phrases, "Se você conhece amantes melhores do que Sue, diga-me quem são."
add_phrase(categories[0].category_id, pressupositions, " Sue conhece pelo menos um amante."

add_cat(categories, "Uso de verbos comparativos",": distinguir, diferenciar, tentar"
add_phrase(categories[0].category_id, phrases, "Você está se diferenciando dos nerds com esses sapatos."
add_phrase(categories[0].category_id, pressupositions, " você é um nerd."
add_phrase(categories[0].category_id, phrases, "Ela está apenas tentando ser diferente."
add_phrase(categories[0].category_id, pressupositions, " Ela não é diferente."
add_phrase(categories[0].category_id, phrases, "Juiz: Você está tentando mostrar desprezo por este tribunal?"
add_phrase(categories[0].category_id, pressupositions, " (por parte do juiz): Flower Belle pode não estar conseguindo demonstrar seu desprezo pelo tribunal."
add_phrase(categories[0].category_id, phrases, "Flower Belle: Não, meritíssimo, estou fazendo o meu melhor para esconder isso!"
add_phrase(categories[0].category_id, pressupositions, " (por parte de Flower Belle): Ela não consegue não demonstrar seu desprezo pela corte."

add_cat(categories, " Comparativo como","uso: ...as x as..."
add_phrase(categories[0].category_id, phrases, "Quando o seu gosto é tão bom quanto o meu, você pode decidir o que comprar."
add_phrase(categories[0].category_id, pressupositions, " Meu gosto é bom."

add_cat(categories, " Uso repetitivo de palavras de sinalização",": também, também, também, novamente, de volta"
add_phrase(categories[0].category_id, phrases, "Se você me disser isso de novo , eu vou gritar."
add_phrase(categories[0].category_id, pressupositions, " Você me disse isso (pelo menos uma vez)."
add_phrase(categories[0].category_id, phrases, "Se você me amasse de volta , eu seria legal."
add_phrase(categories[0].category_id, pressupositions, " você não me ama"
add_phrase(categories[0].category_id, phrases, " Ou fique esperto ou fique quieto."
add_phrase(categories[0].category_id, pressupositions, " Você não é inteligente."

add_cat(categories, " Verbos e advérbios repetitivos","Verbos e advérbios começando com re-. Exemplos: repetidamente, devolver, restaurar, recontar, substituir, renovar"
add_phrase(categories[0].category_id, phrases, "Quando você substituir sua peruca, sairei com você."
add_phrase(categories[0].category_id, pressupositions, " você usa peruca."
add_phrase(categories[0].category_id, phrases, "Quando sua sanidade retornar , conversaremos."
add_phrase(categories[0].category_id, pressupositions, " Você perdeu a sanidade."
add_phrase(categories[0].category_id, phrases, "Ele restaurará a honra e a dignidade ao nosso clube."
add_phrase(categories[0].category_id, pressupositions, "Nosso clube já teve honra e dignidade e não as tem agora."

add_cat(categories, " Uso de qualificadores",": apenas, par, exceto, apenas"

add_phrase(categories[0].category_id, phrases, "É assim que eu sou."
add_phrase(categories[0].category_id, pressupositions, " Só assim posso ser."
add_phrase(categories[0].category_id, phrases, " Só você poderia ser tão denso."
add_phrase(categories[0].category_id, pressupositions, " Você é denso."
add_phrase(categories[0].category_id, phrases, " Até você poderia entender."
add_phrase(categories[0].category_id, pressupositions, " Você é estúpido."
add_phrase(categories[0].category_id, phrases, "Chernobyl foi o desastre do projecto. Em primeiro lugar, os soviéticos tinham projectos muito mais fracos e menos seguros para as suas centrais nucleares do que até mesmo os fabricantes norte-americanos de centrais nucleares."
add_phrase(categories[0].category_id, pressupositions, " Os EUA tinham projetos fracos e inseguros"
add_phrase(categories[0].category_id, phrases, "Ela era apenas uma prostituta."
add_phrase(categories[0].category_id, pressupositions, " Ela não era nada mais."
add_phrase(categories[0].category_id, phrases, "O velho Merton terá que assinar um 'X' porque apenas quatro de nós sabemos escrever."   (Do filme de 2000: "Ó irmão, onde você está")
add_phrase(categories[0].category_id, pressupositions, " Somos mais de quatro. (No filme, quatro músicos estão prestes a ser pagos em dinheiro por um produtor cego - que não sabe quantos deles são - depois de assinarem um contrato.) Observe que "Merton" é um simples nome próprio . Pressuposição do nome (veja acima) de que alguém chamado "Merton" existe neste contexto."

add_cat(categories, " Uso de verbos de mudança de lugar",": vir, ir, sair, chegar, partir, retornar, entrar"
add_phrase(categories[0].category_id, phrases, "Você não será bem-vindo quando voltar ."
add_phrase(categories[0].category_id, pressupositions, " Você vai sair, está saindo ou já saiu."

add_cat(categories, "Uso de verbos e advérbios de mudança de tempo",": começar, terminar, parar, começar, continuar, prosseguir, já, ainda, ainda, mais, irá"
add_phrase(categories[0].category_id, phrases, "Ela ainda não terminou com você ."
add_phrase(categories[0].category_id, pressupositions, " Ela vai terminar com você."
add_phrase(categories[0].category_id, phrases, " Já posso ver que você está mudando."
add_phrase(categories[0].category_id, pressupositions, " Você mudou."
add_phrase(categories[0].category_id, phrases, " O universo durará para sempre?"
add_phrase(categories[0].category_id, pressupositions, " Pode não ser."

add_cat(categories, "Uso de verbos de mudança de estado",": mudar, transformar, transformar em, tornar-se"
add_phrase(categories[0].category_id, phrases, "As coisas parecerão diferentes quando você se tornar um homem."
add_phrase(categories[0].category_id, pressupositions, " Você não é um homem agora."
add_phrase(categories[0].category_id, phrases, "Ela se transformou em uma alma penada do Inferno."
add_phrase(categories[0].category_id, pressupositions, " Ela era anteriormente outra coisa."

add_cat(categories, "Uso de verbos e adjetivos factivos",": estranho, consciente, saber, perceber, arrepender-se"
add_phrase(categories[0].category_id, phrases, "É estranho que você nunca me toque a menos que queira sexo."
add_phrase(categories[0].category_id, pressupositions, "Você nunca me toca a menos que queira sexo."
add_phrase(categories[0].category_id, phrases, "Pare e perceba que eu te amo."
add_phrase(categories[0].category_id, pressupositions, " Você não percebe que eu te amo."

add_cat(categories, "Comentário Uso de adjetivos e advérbios",": sortudo, felizmente, excelente, ótimo, inocentemente, felizmente, necessariamente"
add_phrase(categories[0].category_id, phrases, "É ótimo podermos terminar as frases um do outro."
add_phrase(categories[0].category_id, pressupositions, " Podemos terminar as frases um do outro."

add_cat(categories, "Clausulas condicionais contrafactuais","Verbos com tempo subjuntivo"
add_phrase(categories[0].category_id, phrases, "Se você tivesse me ouvido, não estaria nesta posição."
add_phrase(categories[0].category_id, pressupositions, " Você não me ouviu."
add_phrase(categories[0].category_id, pressupositions, " eu te contei uma coisa."

add_cat(categories, "UUso contrário à expectativa",": deveria"
add_phrase(categories[0].category_id, phrases, "Se você decidir que quer um casamento de verdade, estarei na sala ao lado."
add_phrase(categories[0].category_id, pressupositions, " não espero que você queira um casamento de verdade."

add_cat(categories, "Restrições Selecionais","Atribuir consciência a um objeto inanimado ou um modo de comunicação a uma criatura que não possui esse modo. ("Uma cadeira pode ter sentimentos.") Negar a percepção consciente em seres conscientes ou negar um modo de comunicação ou capacidade a uma criatura que possua esse modo. Excluindo categorias complementares por descrição definida (gênero, raça, religião, etc.). Veja também: Violações de restrição seletiva no metamodelo"
add_phrase(categories[0].category_id, phrases, " As mulheres têm um repertório comportamental maior do que apenas 'lutar ou fugir'."
add_phrase(categories[0].category_id, pressupositions, " Os homens não possuem um repertório comportamental maior do que apenas 'lutar ou fugir'."
add_phrase(categories[0].category_id, phrases, "Para o meu gatinho, sou apenas 'Food Lady' ."
add_phrase(categories[0].category_id, pressupositions, " Um gatinho pode pensar 'Food Lady' (e eu sei o que meu gatinho pensa (leitura de mentes))"

add_cat(categories, "você. Questões",""
add_phrase(categories[0].category_id, phrases, "Quem escondeu minhas chaves?"
add_phrase(categories[0].category_id, pressupositions, " Alguém escondeu minhas chaves."
add_phrase(categories[0].category_id, phrases, "Posso dizer isso?"
add_phrase(categories[0].category_id, pressupositions, "Alguém controla o que posso e não posso dizer."
add_phrase(categories[0].category_id, pressupositions, " Você sabe, ou controla, o que posso e não posso dizer."

add_cat(categories, "Perguntas negativas",""
add_phrase(categories[0].category_id, phrases, "Você não queria falar comigo?"
add_phrase(categories[0].category_id, pressupositions, " pensei que você queria falar comigo."

add_cat(categories, "Perguntas retóricas",""
add_phrase(categories[0].category_id, phrases, "Quem se importa?"
add_phrase(categories[0].category_id, pressupositions, "Ninguém se importa. (ou) eu não me importo."
add_phrase(categories[0].category_id, phrases, "Qual é o seu problema?"
add_phrase(categories[0].category_id, pressupositions, " Você tem um problema."
add_phrase(categories[0].category_id, phrases, "Quem te perguntou ?"
add_phrase(categories[0].category_id, pressupositions, " Você só deve falar quando solicitado."

add_cat(categories, "Espúrio não",""
add_phrase(categories[0].category_id, phrases, "Eu me pergunto se você não está sendo um pouco injusto."
add_phrase(categories[0].category_id, pressupositions, " acho que você está sendo injusto.
add_phrase(categories[0].category_id, phrases, "Ambos os parceiros não deveriam ser responsáveis ​​por relacionamentos destruídos?"
add_phrase(categories[0].category_id, pressupositions, "Ambos os parceiros são responsáveis."

add_cat(categories, "você. Classificação Aristotélica",""
add_phrase(categories[0].category_id, phrases, "Você se mudou duas vezes recentemente. Então, você é um andarilho?"
add_phrase(categories[0].category_id, pressupositions, "Você existe como uma [classe, instância, objeto ou coisa]."
