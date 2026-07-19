#!/usr/bin/env python3
import os
import re
import datetime
import sys
import shutil
import curses

# --- CONFIGURATION & CONSTANTS ---
TEMPLATE_PATH = "blogs/template.html"
BLOG_LIST_PATH = "blog.html"
BLOGS_DIR = "blogs"

# Autocorrect Typos Mapping
AUTOCORRECT_MAP = {
    # Classic transpositions
    "teh": "the",
    "taht": "that",
    "thta": "that",
    "adn": "and",
    "nad": "and",
    "hte": "the",
    "fo": "of",
    "ot": "to",
    "si": "is",
    "ti": "it",
    "eth": "the",
    # Common misspellings
    "recieve": "receive",
    "recieved": "received",
    "recieving": "receiving",
    "seperate": "separate",
    "seperately": "separately",
    "wierd": "weird",
    "comming": "coming",
    "untill": "until",
    "occured": "occurred",
    "occuring": "occurring",
    "occurence": "occurrence",
    "truely": "truly",
    "definately": "definitely",
    "definitly": "definitely",
    "definatly": "definitely",
    "neccessary": "necessary",
    "neccesary": "necessary",
    "necesary": "necessary",
    "embarass": "embarrass",
    "embarassed": "embarrassed",
    "embarassment": "embarrassment",
    "accross": "across",
    "belive": "believe",
    "beleive": "believe",
    "beleif": "belief",
    "belived": "believed",
    "tommorow": "tomorrow",
    "tommorrow": "tomorrow",
    "tomarrow": "tomorrow",
    "writen": "written",
    "writeing": "writing",
    "togo": "to go",
    "alot": "a lot",
    "abit": "a bit",
    "goverment": "government",
    "govermental": "governmental",
    "enviroment": "environment",
    "enviromental": "environmental",
    "shoudl": "should",
    "shold": "should",
    "woudl": "would",
    "wouldl": "would",
    "couldl": "could",
    "aboutt": "about",
    "freind": "friend",
    "freinds": "friends",
    "tought": "thought",
    "thru": "through",
    "happend": "happened",
    "happning": "happening",
    "unforunately": "unfortunately",
    "unfortunatley": "unfortunately",
    "unfortunatly": "unfortunately",
    "beautifuly": "beautifully",
    "beautifull": "beautiful",
    "thier": "their",
    "therfore": "therefore",
    "secon": "second",
    "becuase": "because",
    "beacuse": "because",
    "becasue": "because",
    "biger": "bigger",
    "collegue": "colleague",
    "collegues": "colleagues",
    "congradulations": "congratulations",
    "congrats": "congratulations",
    "arguement": "argument",
    "arguements": "arguments",
    # Contractions
    "dont": "don't",
    "doesnt": "doesn't",
    "cant": "can't",
    "wont": "won't",
    "wouldnt": "wouldn't",
    "couldnt": "couldn't",
    "shouldnt": "shouldn't",
    "isnt": "isn't",
    "arent": "aren't",
    "wasnt": "wasn't",
    "werent": "weren't",
    "hasnt": "hasn't",
    "havent": "haven't",
    "hadnt": "hadn't",
    "didnt": "didn't",
    "doesnt": "doesn't",
    "im": "I'm",
    "ive": "I've",
    "id": "I'd",
    "ill": "I'll",
    "theyre": "they're",
    "theyll": "they'll",
    "theyve": "they've",
    "youre": "you're",
    "youll": "you'll",
    "youve": "you've",
    "youd": "you'd",
    "hes": "he's",
    "shes": "she's",
    "weve": "we've",
    "well": "we'll",
    "wed": "we'd",
    "its": "it's",
    "thats": "that's",
    "whats": "what's",
    "whos": "who's",
    "hows": "how's",
    "wheres": "where's",
    # More misspellings
    "accomodate": "accommodate",
    "acommodate": "accommodate",
    "acheive": "achieve",
    "acheiving": "achieving",
    "acquaintance": "acquaintance",
    "acquaintence": "acquaintance",
    "adress": "address",
    "agressive": "aggressive",
    "agression": "aggression",
    "apparant": "apparent",
    "appearence": "appearance",
    "appriciate": "appreciate",
    "apropriate": "appropriate",
    "argueing": "arguing",
    "assasinate": "assassinate",
    "basicaly": "basically",
    "begining": "beginning",
    "bizzare": "bizarre",
    "calandar": "calendar",
    "calender": "calendar",
    "carribean": "Caribbean",
    "catagory": "category",
    "cemetary": "cemetery",
    "charachter": "character",
    "charcter": "character",
    "cheif": "chief",
    "cieling": "ceiling",
    "coincedence": "coincidence",
    "collumn": "column",
    "commited": "committed",
    "commiting": "committing",
    "comparision": "comparison",
    "completly": "completely",
    "concious": "conscious",
    "concsious": "conscious",
    "consistant": "consistent",
    "continous": "continuous",
    "contraversy": "controversy",
    "conveinent": "convenient",
    "critisism": "criticism",
    "criticise": "criticize",
    "curiousity": "curiosity",
    "defintion": "definition",
    "desparate": "desperate",
    "disapear": "disappear",
    "disapoint": "disappoint",
    "disasterous": "disastrous",
    "discription": "description",
    "doesnt": "doesn't",
    "dramaticaly": "dramatically",
    "easly": "easily",
    "efficency": "efficiency",
    "embarasment": "embarrassment",
    "emerg": "emerge",
    "emphsis": "emphasis",
    "enthuseastic": "enthusiastic",
    "especialy": "especially",
    "essentialy": "essentially",
    "exagerate": "exaggerate",
    "excelent": "excellent",
    "excercise": "exercise",
    "existance": "existence",
    "explaination": "explanation",
    "facilties": "facilities",
    "familier": "familiar",
    "Febuary": "February",
    "febuary": "February",
    "finaly": "finally",
    "foward": "forward",
    "fourty": "forty",
    "frequecy": "frequency",
    "fullfilment": "fulfillment",
    "fundemental": "fundamental",
    "generaly": "generally",
    "guarentee": "guarantee",
    "guarenteed": "guaranteed",
    "guidence": "guidance",
    "happily": "happily",
    "harrassment": "harassment",
    "heirarchy": "hierarchy",
    "humerous": "humorous",
    "hygeine": "hygiene",
    "ignorence": "ignorance",
    "imediately": "immediately",
    "independance": "independence",
    "indispensible": "indispensable",
    "infered": "inferred",
    "intelligance": "intelligence",
    "intresting": "interesting",
    "irresistable": "irresistible",
    "knowlege": "knowledge",
    "leanred": "learned",
    "liason": "liaison",
    "libary": "library",
    "lisence": "license",
    "litrally": "literally",
    "litarally": "literally",
    "logicaly": "logically",
    "maintainence": "maintenance",
    "managment": "management",
    "manuever": "maneuver",
    "medeval": "medieval",
    "millenium": "millennium",
    "mispell": "misspell",
    "misspeled": "misspelled",
    "naturaly": "naturally",
    "neighbourhod": "neighborhood",
    "noticable": "noticeable",
    "ocasion": "occasion",
    "occassion": "occasion",
    "offical": "official",
    "omision": "omission",
    "oportunity": "opportunity",
    "orignal": "original",
    "outragous": "outrageous",
    "overal": "overall",
    "paralel": "parallel",
    "percieve": "perceive",
    "perenial": "perennial",
    "permenent": "permanent",
    "perseverance": "perseverance",
    "phenomemon": "phenomenon",
    "phillsophy": "philosophy",
    "posession": "possession",
    "potatos": "potatoes",
    "practicaly": "practically",
    "predjudice": "prejudice",
    "preveous": "previous",
    "privelege": "privilege",
    "proffesional": "professional",
    "prominant": "prominent",
    "pronounciation": "pronunciation",
    "propoganda": "propaganda",
    "psycology": "psychology",
    "publically": "publicly",
    "questionaire": "questionnaire",
    "realise": "realize",
    "reccomend": "recommend",
    "relevent": "relevant",
    "religous": "religious",
    "remeber": "remember",
    "repitition": "repetition",
    "resistence": "resistance",
    "responsibilty": "responsibility",
    "rythm": "rhythm",
    "sacrafice": "sacrifice",
    "sandwhich": "sandwich",
    "sargeant": "sergeant",
    "scedule": "schedule",
    "sieze": "seize",
    "sentance": "sentence",
    "simaliar": "similar",
    "sincerly": "sincerely",
    "speach": "speech",
    "succesful": "successful",
    "sufficiantly": "sufficiently",
    "suprising": "surprising",
    "supose": "suppose",
    "suprise": "surprise",
    "surpise": "surprise",
    "surveilance": "surveillance",
    "shedule": "schedule",
    "tecnology": "technology",
    "temperture": "temperature",
    "tendancy": "tendency",
    "therefor": "therefore",
    "thorougly": "thoroughly",
    "tomatos": "tomatoes",
    "truley": "truly",
    "tyrany": "tyranny",
    "unkown": "unknown",
    "unecessary": "unnecessary",
    "unusualy": "unusually",
    "usualy": "usually",
    "vaccum": "vacuum",
    "vaguely": "vaguely",
    "valueable": "valuable",
    "varient": "variant",
    "visable": "visible",
    "waht": "what",
    "wehre": "where",
    "whcih": "which",
    "whihc": "which",
    "writting": "writing",
    "yestarday": "yesterday",
    "yeterday": "yesterday",
    "loose": "lose",
    "congradulate": "congratulate",
    "therfore": "therefore",
    "frm": "from",
    "wth": "with",
    "tis": "this",
    "jsut": "just",
    "juts": "just",
    "hwo": "how",
    "owrk": "work",
    "wroks": "works",
    "pubic": "public",
    "tthe": "the",
    "thatn": "than",
    "somthing": "something",
    "eveyone": "everyone",
    "everone": "everyone",
    "somone": "someone",
    "noone": "no one",
    "everday": "everyday",
    "evreything": "everything",
    "everthing": "everything",
    "diferent": "different",
    "diffrent": "different",
    "experiance": "experience",
    "reasearch": "research",
    "reserach": "research",
    "studing": "studying",
    "acualy": "actually",
    "actualy": "actually",
    "probaly": "probably",
    "probabaly": "probably",
    "prolly": "probably",
    "posibly": "possibly",
    "possiblly": "possibly",
    "diffently": "differently",
    "importnat": "important",
    "imporant": "important",
    "seveal": "several",
    "sevral": "several",
    "intrducing": "introducing",
    "comunity": "community",
    "comunication": "communication",
    "communicaiton": "communication",
    "institusion": "institution",
    "increadible": "incredible",
    "incrdeible": "incredible",
    "particuarly": "particularly",
    "partiuclarly": "particularly",
    "apprent": "apparent",
    "obvioulsy": "obviously",
    "obviusly": "obviously",
    "understad": "understand",
    "undrestand": "understand",
    "genrally": "generally",
    "genarally": "generally",
    "espacially": "especially",
    "ecspecially": "especially",
    "wether": "whether",
    "wheter": "whether",
    "untile": "until",
    "arround": "around",
    "wich": "which",
    "beutiful": "beautiful",
    "butiful": "beautiful",
    "haev": "have",
    "hvae": "have",
    "liek": "like",
    "lkie": "like",
    "mkae": "make",
    "maek": "make",
    "amke": "make",
    "taek": "take",
    "tehn": "then",
    "htne": "then",
    "realy": "really",
    "relly": "really",
    "realyl": "really",
    "becasue": "because",
    "baout": "about",
    "abotu": "about",
    "peopel": "people",
    "peolpe": "people",
    "peple": "people",
    "thinkg": "thinking",
    "thinkng": "thinking",
    "knowlege": "knowledge",
    "knwledge": "knowledge",
}

# Fuzzy Autocorrect: minimum edit distance threshold
FUZZY_AUTOCORRECT_MAX_DIST = 1   # Only correct if edit distance == 1
FUZZY_AUTOCORRECT_MIN_LEN  = 5   # Only attempt fuzzy on words >= 5 chars

# Common English vocabulary for fuzzy matching (subset of most frequent words)
# This is used for BOTH fuzzy autocorrect AND word suggestions
ENGLISH_VOCAB = [
    "the","be","to","of","and","a","in","that","have","it","for","not","on",
    "with","he","as","you","do","at","this","but","his","by","from","they",
    "we","say","her","she","or","an","will","my","one","all","would","there",
    "their","what","so","up","out","if","about","who","get","which","go",
    "me","when","make","can","like","time","no","just","him","know","take",
    "people","into","year","your","good","some","could","them","see","other",
    "than","then","now","look","only","come","its","over","think","also",
    "back","after","use","two","how","our","work","first","well","way","even",
    "new","want","because","any","these","give","day","most","us","between",
    "need","large","often","hand","high","place","hold","did","point","world",
    "life","few","north","open","seem","together","next","white","children",
    "begin","got","walk","example","ease","paper","group","always","music",
    "those","both","mark","book","letter","until","mile","river","car","feet",
    "care","second","enough","plain","girl","usual","young","ready","above",
    "ever","red","list","though","feel","talk","bird","soon","body","dog",
    "family","direct","pose","leave","song","measure","door","product","black",
    "short","numeral","class","wind","question","happen","complete","ship",
    "area","half","rock","order","fire","south","problem","piece","told",
    "knew","pass","since","top","whole","king","space","heard","best","hour",
    "better","true","during","hundred","five","remember","step","early","hold",
    "west","ground","interest","reach","fast","verb","sing","listen","row",
    "table","travel","less","morning","ten","simple","several","vowel","toward",
    "word","everything","everyone","someone","something","nothing","nothing",
    "anything","somewhere","nowhere","somehow","sometimes","already","almost",
    "important","actually","probably","really","usually","maybe","perhaps",
    "although","however","therefore","because","whether","through","thought",
    "different","possible","beautiful","situation","experience","knowledge",
    "community","understand","especially","necessary","government","environment",
    "technology","education","philosophy","psychology","comfortable","independent",
    "interesting","immediately","particularly","significantly","relationship",
    "acknowledge","approximately","circumstances","communication","intelligence",
    "development","opportunity","responsibility","understanding","unfortunately",
    "extraordinary","simultaneously","consciousness","consequently","nevertheless",
    "approximately","characteristics","overwhelming","sophisticated","fundamental",
    "nevertheless","apparently","essentially","definitely","absolutely","completely",
    "eventually","recently","currently","generally","originally","naturally",
    "particularly","literally","obviously","seriously","clearly","directly",
    "quickly","slowly","suddenly","finally","simply","truly","deeply","highly",
    "strongly","widely","closely","mostly","partly","hardly","nearly","barely",
    "merely","fairly","quite","rather","pretty","very","just","even","still",
    "again","never","always","often","sometimes","usually","often","rarely",
    "according","regarding","following","including","during","despite","although",
    "meanwhile","moreover","furthermore","additionally","consequently","therefore",
    "however","nevertheless","otherwise","instead","therefore","thus","hence",
    "thereby","whereas","whereby","wherein","thereafter","thereby","therein",
    "believe","achieve","receive","perceive","conceive","retrieve","relieve",
    "achieve","deceive","retrieve","interview","preview","review","overview",
    "writing","reading","thinking","feeling","working","living","learning",
    "growing","building","creating","helping","giving","sharing","caring",
    "knowing","understanding","wondering","discovering","exploring","achieving",
    "becoming","beginning","changing","continuing","developing","following",
    "showing","starting","stopping","happening","looking","making","taking",
    "coming","going","saying","telling","asking","leaving","keeping","trying",
    "wondering","thinking","considering","realizing","believing","expecting",
    "assuming","suggesting","explaining","describing","discussing","analyzing",
    "examining","comparing","contrasting","evaluating","questioning","reflecting",
    "beauty","truth","love","hope","fear","anger","joy","sadness","peace",
    "freedom","justice","equality","courage","wisdom","kindness","honesty",
    "patience","gratitude","compassion","empathy","resilience","creativity",
    "imagination","curiosity","ambition","passion","purpose","meaning","value",
    "society","culture","history","future","present","past","reality","truth",
    "science","nature","human","mind","body","soul","heart","spirit","voice",
    "language","story","journey","path","road","bridge","wall","window","door",
    "light","darkness","shadow","silence","sound","music","rhythm","harmony",
    "power","strength","weakness","challenge","struggle","success","failure",
    "growth","change","transformation","revolution","progress","innovation",
    "problem","solution","question","answer","idea","concept","theory","practice",
]


def levenshtein(s1, s2):
    """Compute Levenshtein edit distance between two strings."""
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if not s2:
        return len(s1)
    prev = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            curr.append(min(prev[j + 1] + 1,
                            curr[j] + 1,
                            prev[j] + (c1 != c2)))
        prev = curr
    return prev[-1]


def check_fuzzy_autocorrect(word):
    """Attempt to fuzzy-match a word against the autocorrect map and common vocabulary.
    Returns the suggested correction or None."""
    if len(word) < FUZZY_AUTOCORRECT_MIN_LEN:
        return None
    lower = word.lower()
    # Don't fuzzy-correct words that look like proper nouns (all caps)
    if word.isupper() and len(word) > 2:
        return None
    best_word = None
    best_dist = FUZZY_AUTOCORRECT_MAX_DIST + 1
    # Check against known-good vocabulary
    for candidate in ENGLISH_VOCAB:
        if abs(len(candidate) - len(lower)) > FUZZY_AUTOCORRECT_MAX_DIST:
            continue
        d = levenshtein(lower, candidate)
        if d < best_dist:
            best_dist = d
            best_word = candidate
        elif d == best_dist and best_word is not None:
            # Prefer longer candidate (more specific match)
            if len(candidate) > len(best_word):
                best_word = candidate
    if best_dist <= FUZZY_AUTOCORRECT_MAX_DIST and best_word and best_word != lower:
        return best_word
    return None


def get_suggestions(partial_word, n=5):
    """Return up to n vocabulary words that start with partial_word (case-insensitive)."""
    if not partial_word or len(partial_word) < 2:
        return []
    lower = partial_word.lower()
    # First: exact prefix matches from AUTOCORRECT_MAP values (quality words)
    seen = set()
    results = []
    for val in AUTOCORRECT_MAP.values():
        if val.lower().startswith(lower) and val.lower() != lower:
            key = val.lower()
            if key not in seen:
                seen.add(key)
                results.append(val)
    # Then: prefix matches from ENGLISH_VOCAB
    for word in ENGLISH_VOCAB:
        if word.startswith(lower) and word != lower:
            if word not in seen:
                seen.add(word)
                results.append(word)
    # Sort: shorter words first (more likely completions)
    results.sort(key=lambda w: (len(w), w))
    return results[:n]


# --- PARSING & MARKDOWN FUNCTIONS ---
def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

def parse_inline_markdown(text):
    # Lightweight inline markdown parser
    # Bold: **bold**
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic: *italic*
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Inline links: [text](url)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', text)
    return text

def wrap_block_text(text, width):
    """Word-wraps the block's text and returns list of lines, plus a list of
    character coordinates mapped to (line_idx, col_idx) in the wrapped output."""
    if not text:
        return [""], [(0, 0)]
        
    tokens = re.split(r'(\s+)', text)
    lines = []
    char_positions = []
    
    current_line = ""
    current_line_idx = 0
    
    for token in tokens:
        if not token:
            continue
        if len(current_line) + len(token) <= width or not current_line:
            # Fits in current line
            for char in token:
                char_positions.append((current_line_idx, len(current_line)))
                current_line += char
        else:
            # New line
            lines.append(current_line)
            current_line_idx += 1
            current_line = ""
            for char in token:
                char_positions.append((current_line_idx, len(current_line)))
                current_line += char
                
    if current_line or not lines:
        lines.append(current_line)
        
    # Append mapping for cursor_pos == len(text) (end of text)
    if char_positions:
        last_line, last_col = char_positions[-1]
        if last_col + 1 < width:
            char_positions.append((last_line, last_col + 1))
        else:
            char_positions.append((last_line + 1, 0))
    else:
        char_positions.append((0, 0))
        
    return lines, char_positions

def find_best_cursor_pos(positions, target_line, target_col):
    """Finds the index in positions closest to target_col on target_line."""
    best_idx = 0
    min_dist = 999999
    for idx, (l, c) in enumerate(positions):
        if l == target_line:
            dist = abs(c - target_col)
            if dist < min_dist:
                min_dist = dist
                best_idx = idx
    return best_idx

def _extract_word_before_space(text, pos):
    """Extract the word that ends just before the cursor (which just typed a space).
    Returns (start_idx, word) or (None, None)."""
    if pos < 2:
        return None, None
    idx = pos - 2  # character before the space
    while idx >= 0:
        char = text[idx]
        if not (char.isalpha() or char == "'"):
            break
        idx -= 1
    start_idx = idx + 1
    word = text[start_idx:pos - 1]
    return (start_idx, word) if word else (None, None)


def check_autocorrect(text, pos, enabled):
    """Checks the word just completed (before space) for typos and replaces it.
    First tries the AUTOCORRECT_MAP; if no match, tries fuzzy correction.
    Returns (new_text, new_pos, correction_tuple_or_None, was_fuzzy).
    """
    if not enabled or pos < 2:
        return text, pos, None, False

    start_idx, word = _extract_word_before_space(text, pos)
    if not word:
        return text, pos, None, False

    lower_word = word.lower()

    # 1) Exact dictionary match
    if lower_word in AUTOCORRECT_MAP:
        rep = AUTOCORRECT_MAP[lower_word]
        # Preserve capitalisation
        if word.isupper():
            rep = rep.upper()
        elif word[0].isupper():
            rep = rep[0].upper() + rep[1:]
        new_text = text[:start_idx] + rep + text[pos - 1:]
        new_pos = pos + len(rep) - len(word)
        return new_text, new_pos, (word, rep), False

    # 2) Fuzzy fallback (only for longer words to avoid false positives)
    fuzzy = check_fuzzy_autocorrect(word)
    if fuzzy:
        rep = fuzzy
        if word[0].isupper():
            rep = rep[0].upper() + rep[1:]
        new_text = text[:start_idx] + rep + text[pos - 1:]
        new_pos = pos + len(rep) - len(word)
        return new_text, new_pos, (word, rep), True

    return text, pos, None, False


def get_current_partial_word(text, pos):
    """Return the partial word currently being typed at cursor position."""
    if pos == 0 or (pos > 0 and text[pos - 1] == ' '):
        return ""
    idx = pos - 1
    while idx >= 0 and (text[idx].isalpha() or text[idx] == "'"):
        idx -= 1
    return text[idx + 1:pos]

def generate_block_html(block, blog_title=""):
    btype = block['type']
    text = block['text']
    if btype == 'paragraph':
        parsed = parse_inline_markdown(text)
        return f"    <p>\n      {parsed}\n    </p>"
    elif btype == 'heading':
        parsed = parse_inline_markdown(text)
        return f"    <h2>{parsed}</h2>"
    elif btype == 'quote':
        parsed = parse_inline_markdown(text)
        return f"    <blockquote>\n      \"{parsed}\"\n    </blockquote>"
    elif btype == 'image':
        src = ""
        caption = ""
        if "Src:" in text:
            match_src = re.search(r'Src:\s*(.*?)(?:\s*\|\s*Cap:|$)', text)
            if match_src:
                src = match_src.group(1).strip()
            match_cap = re.search(r'Cap:\s*(.*)', text)
            if match_cap:
                caption = match_cap.group(1).strip()
        else:
            src = text.strip()
            
        img_html = f"    <figure>\n      <img src=\"{src}\" alt=\"{blog_title}\">"
        if caption:
            img_html += f"\n      <figcaption>{caption}</figcaption>"
        img_html += "\n    </figure>"
        return img_html
    elif btype == 'video':
        return f"    <div class=\"video-container\">\n      {text}\n    </div>"
    elif btype == 'music':
        return f"    <div class=\"media-embed\">\n      {text}\n    </div>"
    return ""

def save_blog(title, category, excerpt, blocks):
    """Compiles and generates the blog post html and updates listings."""
    date_now = datetime.datetime.now().strftime("%B %d, %Y")
    iso_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    slug = slugify(title)
    if not slug:
        return False, "Slug is empty. Enter a valid Title."
        
    file_path = os.path.join(BLOGS_DIR, f"{slug}.html")
    full_content = "\n\n".join([generate_block_html(b, title) for b in blocks])
    
    try:
        with open(TEMPLATE_PATH, "r") as f:
            template = f.read()
    except FileNotFoundError:
        return False, f"Template {TEMPLATE_PATH} not found."
        
    # Regex replacements
    page = re.sub(r'<title>.*?</title>', f'<title>{title} — Farouk Ashraf</title>', template)
    page = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{excerpt}">', page)
    page = re.sub(r'<span class="hero-tag">.*?</span>', f'<span class="hero-tag">{category}</span>', page)
    page = re.sub(r'<h1 class="blog-post-title">.*?</h1>', f'<h1 class="blog-post-title">{title}</h1>', page)
    page = re.sub(r'Published on .*? — Written by Farouk Ashraf', f'Published on {date_now} — Written by Farouk Ashraf', page)
    
    body_pattern = r'(<div class="blog-content-body">).*?(</div>)'
    page = re.sub(body_pattern, rf'\1\n{full_content}\n  \2', page, flags=re.DOTALL)
    
    canonical = f'https://farouk-pharmd.github.io/website/blogs/{slug}.html'
    page = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{canonical}">', page)
    
    page = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{canonical}">', page)
    page = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title} — Farouk Ashraf">', page)
    page = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{excerpt}">', page)
    
    page = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{title} — Farouk Ashraf">', page)
    page = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{excerpt}">', page)
    
    page = re.sub(r'<meta property="article:published_time" content=".*?">', f'<meta property="article:published_time" content="{iso_date}">', page)
    
    # Write blog page
    try:
        os.makedirs(BLOGS_DIR, exist_ok=True)
        with open(file_path, "w") as f:
            f.write(page)
    except Exception as e:
        return False, f"Failed to write blog: {e}"
        
    # Update listings page (blog.html)
    try:
        if os.path.exists(BLOG_LIST_PATH):
            with open(BLOG_LIST_PATH, "r") as f:
                list_page = f.read()
                
            with open(f"{BLOG_LIST_PATH}.bak", "w") as f:
                f.write(list_page)
                
            new_card = f"""
    <a href="blogs/{slug}.html" class="blog-card reveal">
      <div class="blog-card-meta">
        <span class="blog-date">{date_now}</span>
        <span class="blog-tag">{category}</span>
      </div>
      <h3>{title}</h3>
      <p class="blog-excerpt">
        {excerpt}
      </p>
      <span class="blog-read-more">Read Entry →</span>
    </a>"""
            
            card_href = f'blogs/{slug}.html'
            if card_href in list_page:
                card_pattern = r'<a href="blogs/' + re.escape(slug) + r'\.html".*?</a>'
                updated_list = re.sub(card_pattern, new_card, list_page, flags=re.DOTALL)
            else:
                grid_pattern = r'(<div class="blog-grid">)'
                updated_list = re.sub(grid_pattern, rf'\1{new_card}', list_page)
                
            with open(BLOG_LIST_PATH, "w") as f:
                f.write(updated_list)
        else:
            return False, f"Blog list file {BLOG_LIST_PATH} not found."
    except Exception as e:
        return False, f"Failed to update blog list: {e}"
        
    return True, file_path


# --- ASCII CAT ART LIBRARY ---
LOLCATS = [
    # Cat 1: classic sitting cat
    [
        r" /\_/\  ",
        r"( o.o ) ",
        r" > ^ <  ",
        r"(_____)  ",
    ],
    # Cat 2: happy cat
    [
        r" /\_/\  ",
        r"( ^.^ ) ",
        r"  >{>   ",
        r" (___) ",
    ],
    # Cat 3: sleeping cat
    [
        r"  /\_/\ ",
        r" (-.-) z",
        r"  >//<  ",
        r" (___) ",
    ],
    # Cat 4: loaf cat
    [
        r"  /\_/\ ",
        r" ( ._.) ",
        r" (  v  )",
        r"  ^   ^ ",
    ],
    # Cat 5: shocked cat
    [
        r" /\_/\  ",
        r"( O.O ) ",
        r" \m/\m/ ",
        r" (___) ",
    ],
    # Cat 6: small kitty
    [
        r"|\_/| ",
        r"|q p|/",
        r"=( Y )=",
        r" )   ( ",
    ],
    # Cat 7: grumpy
    [
        r" /\_/\ ",
        r"( >.< )",
        r" (___) ",
        r"  | |  ",
    ],
    # Cat 8: waving
    [
        r"  /\_/\ ",
        r" ( ^v^)~",
        r"  >/><  ",
        r" (___) ",
    ],
]

# Tiny 2-line cats for drifting background
MINI_CATS = [
    [r"/\_/\\", r"(o.o)"],
    [r"/\_/\\", r"(^.^)"],
    [r"/\_/\\", r"(-.-)z"],
    [r"/\_/\\", r"(>.<)"],
    [r"|\_/|", r"|q p|"],
    [r"  /\_", r"( ^v)"],
    [r"/\_/\\", r"(O.O)"],
    [r"/\_/\\", r"( ._)"],
]

CAT_CAPTIONS = [
    "im in ur editor, riting ur blogz",
    "ceiling cat watches ur typos",
    "do not want autocorrect",
    "halp im stuck in terminal",
    "oh hai! i can has essay?",
    "invisible keyboard is invisible",
    "dis is mah blog naow",
    "u no save?? i judge u",
    "typing intensifies",
    "420 words per meowr",
]


# --- TUI DRAW & BOX FUNCTIONS ---
def draw_box(stdscr, y, x, h, w, title=None, color_pair=3):
    """Draws a consistent single-line border around coordinates.
    color_pair: 3 = muted (default), 2 = accent/active
    """
    tl, tr, bl, br = "┌", "┐", "└", "┘"
    hl, vl = "─", "│"
    attr = curses.color_pair(color_pair)

    for cy in range(y + 1, y + h - 1):
        try:
            stdscr.addch(cy, x, vl, attr)
            stdscr.addch(cy, x + w - 1, vl, attr)
        except curses.error:
            pass

    for cx in range(x + 1, x + w - 1):
        try:
            stdscr.addch(y, cx, hl, attr)
            stdscr.addch(y + h - 1, cx, hl, attr)
        except curses.error:
            pass

    try:
        stdscr.addch(y, x, tl, attr)
        stdscr.addch(y, x + w - 1, tr, attr)
        stdscr.addch(y + h - 1, x, bl, attr)
        stdscr.addch(y + h - 1, x + w - 1, br, attr)
    except curses.error:
        pass

    if title:
        title_str = f" {title} "
        tx = x + (w - len(title_str)) // 2
        if tx > x:
            try:
                stdscr.addstr(y, tx, title_str, curses.color_pair(2) | curses.A_BOLD)
            except curses.error:
                pass

def is_backspace(ch):
    """Detects backspace character strings or integer key codes across terminals."""
    if isinstance(ch, str):
        return ord(ch) in [127, 8]
    elif isinstance(ch, int):
        return ch in [curses.KEY_BACKSPACE, 127, 8, 263]
    return False


# --- BACKGROUND ANIMATION HELPERS ---
def _safe_addstr(stdscr, y, x, text, attr=0):
    """addstr that silently ignores out-of-bounds writes."""
    h, w = stdscr.getmaxyx()
    if y < 0 or y >= h:
        return
    # clip text to available width
    avail = w - x
    if avail <= 0:
        return
    try:
        stdscr.addstr(y, x, text[:avail], attr)
    except curses.error:
        pass


def draw_drifting_cats(stdscr, frame, cat_positions):
    """Draw mini ASCII cats drifting left-to-right across the screen background.
    cat_positions: list of dicts with keys x, y, cat_idx, speed, caption_visible
    Returns updated cat_positions.
    """
    h, w = stdscr.getmaxyx()
    import math

    for cp in cat_positions:
        # Erase previous position by overwriting with spaces
        old_x = int(cp['x'])
        cat = MINI_CATS[cp['cat_idx'] % len(MINI_CATS)]
        cat_w = max(len(line) for line in cat)
        for li, line in enumerate(cat):
            _safe_addstr(stdscr, cp['y'] + li, old_x, " " * (cat_w + 1))

        # Advance
        cp['x'] += cp['speed']
        # Wrap around
        if cp['x'] > w + 4:
            cp['x'] = -(cat_w + 2)
            cp['y'] = max(1, cp['y'])  # keep same row

        # Draw at new position
        new_x = int(cp['x'])
        color = curses.color_pair(cp.get('color', 6)) | curses.A_DIM
        for li, line in enumerate(cat):
            _safe_addstr(stdscr, cp['y'] + li, new_x, line, color)

    return cat_positions


def make_cat_positions(h, w, count=6):
    """Generate initial cat positions spread across the screen."""
    import random
    positions = []
    used_rows = set()
    for i in range(count):
        for attempt in range(20):
            row = random.randint(2, max(3, h - 4))
            if row not in used_rows and row + 1 not in used_rows:
                used_rows.add(row)
                used_rows.add(row + 1)
                break
        positions.append({
            'x': random.randint(-8, w),
            'y': row,
            'cat_idx': i % len(MINI_CATS),
            'speed': 0.25 + (i % 4) * 0.12,
            'color': (i % 3) + 4,  # pairs 4, 5, 6
        })
    return positions


# --- DIALOGS & OVERLAYS ---
def draw_splash(stdscr, frame, splash_cat_idx):
    """Draws the minimalistic splash screen with one centered rotating cat."""
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    draw_box(stdscr, 1, 1, h - 2, w - 2, " MEIN LOUNGE — TYPOGRAPHY ENGINE ")

    logo = [
        r"   __  ___     _      __     ",
        r"  /  |/  /__  (_)__  / /     ",
        r" / /|_/ / _ \/ / _ \/ /___  ",
        r"/_/  /_/\___/_/_//_/____/  ",
        r"  L  O  U  N  G  E          ",
    ]

    logo_y = max(3, h // 2 - 8)
    for i, line in enumerate(logo):
        start_x = max(2, (w - len(line)) // 2)
        _safe_addstr(stdscr, logo_y + i, start_x, line, curses.color_pair(2) | curses.A_BOLD)

    subtitle = "E S S A Y   E D I T O R   v 3 . 0"
    _safe_addstr(stdscr, logo_y + len(logo) + 1, max(2, (w - len(subtitle)) // 2),
                 subtitle, curses.color_pair(3))

    # ---- Single rotating lolcat, centered ----
    cat_art = LOLCATS[splash_cat_idx % len(LOLCATS)]
    caption = CAT_CAPTIONS[splash_cat_idx % len(CAT_CAPTIONS)]
    cat_w = max(len(cl) for cl in cat_art)
    cat_x = max(2, (w - cat_w) // 2)
    cat_y = logo_y + len(logo) + 3
    for li, cl in enumerate(cat_art):
        _safe_addstr(stdscr, cat_y + li, cat_x, cl, curses.color_pair(4) | curses.A_DIM)
    _safe_addstr(stdscr, cat_y + len(cat_art), max(2, (w - len(caption) - 4) // 2),
                 f"~ {caption} ~", curses.color_pair(3) | curses.A_DIM)

    # ---- Progress bar ----
    percent = min(frame * 10, 100)
    bar_width = min(36, w - 16)
    filled = int(bar_width * percent / 100)
    bar = "█" * filled + "░" * (bar_width - filled)

    stages = [
        "Feeding the cats...",
        "Loading Lexicon Dictionary...",
        "Setting up block templates...",
        "Teaching cats to type...",
        "Herding cats into columns...",
        "Tuning kerning engines...",
        "Bribing cats with treats...",
        "Injecting editorial soul...",
        "Polishing terminal buffers...",
        "Typography System Ready! meow."
    ]
    stage_text = stages[min(frame, len(stages) - 1)]

    progress_y = cat_y + len(cat_art) + 2
    bar_text = f"[{bar}] {percent}%"
    _safe_addstr(stdscr, progress_y, max(2, (w - len(bar_text)) // 2),
                 bar_text, curses.color_pair(2))
    _safe_addstr(stdscr, progress_y + 1, max(2, (w - len(stage_text)) // 2),
                 stage_text, curses.color_pair(3))

    if frame >= 10:
        prompt = "◆ PRESS ANY KEY TO BEGIN ◆"
        if (frame // 2) % 2 == 0:
            _safe_addstr(stdscr, progress_y + 3,
                         max(2, (w - len(prompt)) // 2),
                         prompt, curses.color_pair(2) | curses.A_BOLD)
        else:
            _safe_addstr(stdscr, progress_y + 3,
                         max(2, (w - len(prompt)) // 2),
                         " " * len(prompt))

    stdscr.refresh()

def draw_input_field(stdscr, y, x, w, label, text, offset, pos, is_active):
    """Draws a consistently bordered input box with an embedded label and scrolling text."""
    # Unified single-line style; active = accent color, inactive = muted
    color_pair_id = 2 if is_active else 3
    draw_box(stdscr, y, x, 3, w, title=label, color_pair=color_pair_id)

    # Scrolling visible segment tracking
    field_w = w - 4
    if pos < offset:
        offset = pos
    elif pos >= offset + field_w:
        offset = pos - field_w + 1

    disp_text = text[offset: offset + field_w]
    disp_text += " " * (field_w - len(disp_text))

    text_attr = curses.color_pair(1) | curses.A_REVERSE if is_active else curses.color_pair(1)
    try:
        stdscr.addstr(y + 1, x + 2, disp_text, text_attr)
    except curses.error:
        pass

    return offset

def edit_metadata_dialog(stdscr, title, category, excerpt, draw_bg_callback):
    """Brings up a dialog layout to input essay metadata details."""
    curses.curs_set(1)
    h, w = stdscr.getmaxyx()
    box_w = max(60, w - 8)
    box_h = 16
    box_y = (h - box_h) // 2
    box_x = (w - box_w) // 2

    f_title = title
    f_category = category
    f_excerpt = excerpt

    active_field = 0  # 0: title, 1: category, 2: excerpt, 3: Save, 4: Cancel

    pos_title = len(f_title)
    pos_category = len(f_category)
    pos_excerpt = len(f_excerpt)

    offset_title = 0
    offset_category = 0
    offset_excerpt = 0

    while True:
        stdscr.erase()
        draw_bg_callback()  # Redraw the background editor

        # Shadow effect (offset 1,2)
        for r in range(box_h):
            for c in range(box_w):
                sy, sx = box_y + r + 1, box_x + c + 2
                if 0 <= sy < h and 0 <= sx < w:
                    try:
                        stdscr.addch(sy, sx, " ", curses.A_DIM | curses.color_pair(3))
                    except curses.error:
                        pass

        # Outer dialog box — accent color (active)
        draw_box(stdscr, box_y, box_x, box_h, box_w,
                 " EDIT ESSAY METADATA ", color_pair=2)

        # Small lolcat in top-right corner of dialog
        tiny_cat = LOLCATS[2]  # sleeping cat
        tc_x = box_x + box_w - 11
        tc_color = curses.color_pair(4) | curses.A_DIM
        for li, cl in enumerate(tiny_cat[:2]):
            _safe_addstr(stdscr, box_y + 1 + li, tc_x, cl, tc_color)

        # Draw input fields
        offset_title = draw_input_field(
            stdscr, box_y + 2, box_x + 3, box_w - 6,
            "Title", f_title, offset_title, pos_title, active_field == 0)
        offset_category = draw_input_field(
            stdscr, box_y + 6, box_x + 3, box_w - 6,
            "Category", f_category, offset_category, pos_category, active_field == 1)
        offset_excerpt = draw_input_field(
            stdscr, box_y + 10, box_x + 3, box_w - 6,
            "Excerpt", f_excerpt, offset_excerpt, pos_excerpt, active_field == 2)

        # Action Buttons
        btn_save_attr = curses.color_pair(2) | curses.A_REVERSE if active_field == 3 else curses.color_pair(2) | curses.A_BOLD
        btn_cancel_attr = curses.color_pair(3) | curses.A_REVERSE if active_field == 4 else curses.color_pair(3)

        _safe_addstr(stdscr, box_y + 13, box_x + box_w // 2 - 12,
                     "┤ SAVE ├", btn_save_attr)
        _safe_addstr(stdscr, box_y + 13, box_x + box_w // 2 + 2,
                     "┤ CANCEL ├", btn_cancel_attr)

        # Hint line
        hint = "Tab/↑↓ navigate  ·  Enter confirm  ·  Esc cancel"
        _safe_addstr(stdscr, box_y + box_h - 2, box_x + 3,
                     hint[:box_w - 6], curses.color_pair(3) | curses.A_DIM)

        # Place Cursor
        try:
            if active_field == 0:
                stdscr.move(box_y + 3, box_x + 5 + (pos_title - offset_title))
            elif active_field == 1:
                stdscr.move(box_y + 7, box_x + 5 + (pos_category - offset_category))
            elif active_field == 2:
                stdscr.move(box_y + 11, box_x + 5 + (pos_excerpt - offset_excerpt))
            elif active_field == 3:
                stdscr.move(box_y + 13, box_x + box_w // 2 - 11)
            elif active_field == 4:
                stdscr.move(box_y + 13, box_x + box_w // 2 + 3)
        except curses.error:
            pass

        stdscr.refresh()

        try:
            ch = stdscr.get_wch()
        except curses.error:
            continue

        if ch == '\x1b':  # ESC
            curses.curs_set(0)
            return None
        elif ch == '\t':  # Tab
            active_field = (active_field + 1) % 5
        elif isinstance(ch, int) and ch == curses.KEY_BTAB:  # Shift+Tab
            active_field = (active_field - 1) % 5
        elif isinstance(ch, int) and ch == curses.KEY_DOWN:
            active_field = (active_field + 1) % 5
        elif isinstance(ch, int) and ch == curses.KEY_UP:
            active_field = (active_field - 1) % 5
        elif ch == '\n' or ch == '\r':
            if active_field == 3:
                curses.curs_set(0)
                return f_title.strip(), f_category.strip(), f_excerpt.strip()
            elif active_field == 4:
                curses.curs_set(0)
                return None
            else:
                active_field = (active_field + 1) % 5
        elif is_backspace(ch):
            if active_field == 0:
                if pos_title > 0:
                    f_title = f_title[:pos_title - 1] + f_title[pos_title:]
                    pos_title -= 1
            elif active_field == 1:
                if pos_category > 0:
                    f_category = f_category[:pos_category - 1] + f_category[pos_category:]
                    pos_category -= 1
            elif active_field == 2:
                if pos_excerpt > 0:
                    f_excerpt = f_excerpt[:pos_excerpt - 1] + f_excerpt[pos_excerpt:]
                    pos_excerpt -= 1
        elif isinstance(ch, int) and ch == curses.KEY_LEFT:
            if active_field == 0:
                pos_title = max(0, pos_title - 1)
            elif active_field == 1:
                pos_category = max(0, pos_category - 1)
            elif active_field == 2:
                pos_excerpt = max(0, pos_excerpt - 1)
        elif isinstance(ch, int) and ch == curses.KEY_RIGHT:
            if active_field == 0:
                pos_title = min(len(f_title), pos_title + 1)
            elif active_field == 1:
                pos_category = min(len(f_category), pos_category + 1)
            elif active_field == 2:
                pos_excerpt = min(len(f_excerpt), pos_excerpt + 1)
        elif isinstance(ch, str) and ord(ch) >= 32 and ord(ch) != 127:
            if active_field == 0:
                if len(f_title) < 200:
                    f_title = f_title[:pos_title] + ch + f_title[pos_title:]
                    pos_title += 1
            elif active_field == 1:
                if len(f_category) < 200:
                    f_category = f_category[:pos_category] + ch + f_category[pos_category:]
                    pos_category += 1
            elif active_field == 2:
                if len(f_excerpt) < 500:
                    f_excerpt = f_excerpt[:pos_excerpt] + ch + f_excerpt[pos_excerpt:]
                    pos_excerpt += 1

def input_dialog(stdscr, title, prompt_text, default_val="", draw_bg_callback=None):
    """Draws a centered single text prompt editor input window."""
    curses.curs_set(1)
    h, w = stdscr.getmaxyx()
    box_w = max(60, w - 8)
    box_h = 7
    box_y = (h - box_h) // 2
    box_x = (w - box_w) // 2

    val = default_val
    pos = len(val)
    offset = 0

    while True:
        stdscr.erase()
        if draw_bg_callback:
            draw_bg_callback()

        # Shadow
        for r in range(box_h):
            for c in range(box_w):
                sy, sx = box_y + r + 1, box_x + c + 2
                if 0 <= sy < h and 0 <= sx < w:
                    try:
                        stdscr.addch(sy, sx, " ", curses.A_DIM | curses.color_pair(3))
                    except curses.error:
                        pass

        draw_box(stdscr, box_y, box_x, box_h, box_w, title, color_pair=2)
        offset = draw_input_field(
            stdscr, box_y + 2, box_x + 3, box_w - 6,
            prompt_text, val, offset, pos, True)

        hint = "Enter to confirm  ·  Esc to cancel"
        _safe_addstr(stdscr, box_y + box_h - 2, box_x + 3,
                     hint[:box_w - 6], curses.color_pair(3) | curses.A_DIM)

        try:
            stdscr.move(box_y + 3, box_x + 5 + (pos - offset))
        except curses.error:
            pass
        stdscr.refresh()

        try:
            ch = stdscr.get_wch()
        except curses.error:
            continue

        if ch == '\x1b':  # ESC
            curses.curs_set(0)
            return None
        elif ch == '\n' or ch == '\r':
            curses.curs_set(0)
            return val.strip()
        elif is_backspace(ch):
            if pos > 0:
                val = val[:pos - 1] + val[pos:]
                pos -= 1
        elif isinstance(ch, int) and ch == curses.KEY_LEFT:
            pos = max(0, pos - 1)
        elif isinstance(ch, int) and ch == curses.KEY_RIGHT:
            pos = min(len(val), pos + 1)
        elif isinstance(ch, str) and ord(ch) >= 32 and ord(ch) != 127:
            if len(val) < 2000:
                val = val[:pos] + ch + val[pos:]
                pos += 1


def menu_dialog(stdscr, title, items, default_idx=0, draw_bg_callback=None):
    """Draws a pop-up selection window that responds to keys and arrows."""
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    box_w = max(len(t) for t in items) + 8
    box_w = max(box_w, len(title) + 10)
    box_h = len(items) + 4

    box_y = (h - box_h) // 2
    box_x = (w - box_w) // 2

    selected_idx = default_idx

    while True:
        stdscr.erase()
        if draw_bg_callback:
            draw_bg_callback()

        # Shadow
        for r in range(box_h):
            for c in range(box_w):
                sy, sx = box_y + r + 1, box_x + c + 2
                if 0 <= sy < h and 0 <= sx < w:
                    try:
                        stdscr.addch(sy, sx, " ", curses.A_DIM | curses.color_pair(3))
                    except curses.error:
                        pass

        draw_box(stdscr, box_y, box_x, box_h, box_w, title, color_pair=2)

        for idx, item in enumerate(items):
            iy = box_y + 2 + idx
            ix = box_x + 3
            if item.startswith("───"):
                _safe_addstr(stdscr, iy, ix, item[:box_w - 6], curses.color_pair(3) | curses.A_DIM)
            else:
                attr = curses.color_pair(2) | curses.A_REVERSE if idx == selected_idx else curses.color_pair(1)
                _safe_addstr(stdscr, iy, ix, " " * (box_w - 6))
                _safe_addstr(stdscr, iy, ix, item[:box_w - 6], attr)

        _safe_addstr(stdscr, box_y + box_h - 2, box_x + 3,
                     "↑↓ navigate  ·  Enter select  ·  Esc cancel"[:box_w - 6],
                     curses.color_pair(3) | curses.A_DIM)

        stdscr.refresh()

        try:
            ch = stdscr.get_wch()
        except curses.error:
            continue

        if ch == '\x1b':  # ESC
            return None
        elif isinstance(ch, int) and ch == curses.KEY_UP:
            selected_idx = (selected_idx - 1) % len(items)
            while items[selected_idx].startswith("───"):
                selected_idx = (selected_idx - 1) % len(items)
        elif isinstance(ch, int) and ch == curses.KEY_DOWN:
            selected_idx = (selected_idx + 1) % len(items)
            while items[selected_idx].startswith("───"):
                selected_idx = (selected_idx + 1) % len(items)
        elif ch == '\n' or ch == '\r':
            return selected_idx
        elif isinstance(ch, str) and len(ch) == 1:
            char = ch.lower()
            for idx, item in enumerate(items):
                if item.startswith(f"[{char}]") or item.startswith(f"[{char.upper()}]"):
                    return idx

def show_help_dialog(stdscr, draw_bg_callback):
    """Overlay explaining keyboard key combinations."""
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    box_h = 22
    box_w = 68
    box_y = (h - box_h) // 2
    box_x = (w - box_w) // 2

    stdscr.erase()
    draw_bg_callback()

    # Shadow
    for r in range(box_h):
        for c in range(box_w):
            sy, sx = box_y + r + 1, box_x + c + 2
            if 0 <= sy < h and 0 <= sx < w:
                try:
                    stdscr.addch(sy, sx, " ", curses.A_DIM | curses.color_pair(3))
                except curses.error:
                    pass

    draw_box(stdscr, box_y, box_x, box_h, box_w,
             " KEYBOARD SHORTCUTS ", color_pair=2)

    shortcuts = [
        ("Ctrl+/",     "Open Action / Insert Menu (or Ctrl+K)"),
        ("Ctrl+S",     "Save Essay & Compile Website"),
        ("Ctrl+E",     "Edit Essay Metadata (Title, etc.)"),
        ("Ctrl+A",     "Toggle Autocorrect (ON / OFF)"),
        ("Ctrl+Z",     "Undo last autocorrect"),
        ("Ctrl+D",     "Delete Current Block"),
        ("Ctrl+U",     "Move Current Block UP"),
        ("Ctrl+N",     "Move Current Block DOWN"),
        ("Ctrl+T",     "Show this help panel"),
        ("Ctrl+Q",     "Quit Editor (checks for changes)"),
        ("Enter",      "Split text / Insert paragraph block"),
        ("Arrows",     "Navigate letters/words & blocks"),
        ("Backspace",  "Delete char (merges blocks at pos 0)"),
        ("Tab",        "Accept first word suggestion"),
        ("Ctrl+→ / ←", "Cycle through word suggestions"),
    ]

    for idx, (key, desc) in enumerate(shortcuts):
        _safe_addstr(stdscr, box_y + 2 + idx, box_x + 3,
                     f"{key:<12}", curses.color_pair(2) | curses.A_BOLD)
        _safe_addstr(stdscr, box_y + 2 + idx, box_x + 16,
                     f"│ {desc}", curses.color_pair(1))

    # Small cat at bottom of help dialog
    help_cat = LOLCATS[0]
    hc_x = box_x + box_w - 12
    hc_y = box_y + box_h - 6
    for li, cl in enumerate(help_cat[:3]):
        _safe_addstr(stdscr, hc_y + li, hc_x, cl,
                     curses.color_pair(5) | curses.A_DIM)

    _safe_addstr(stdscr, box_y + box_h - 2,
                 box_x + (box_w - 28) // 2,
                 "┤ press any key to close ├",
                 curses.color_pair(3))
    stdscr.refresh()
    stdscr.getch()

def save_animation(stdscr):
    """Draws the animated retro file building progress screen with a celebrating cat."""
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    box_h = 12
    box_w = 54
    box_y = (h - box_h) // 2
    box_x = (w - box_w) // 2

    stdscr.nodelay(True)
    steps = [
        "Analyzing markdown segments...",
        "Applying editorial theme replacements...",
        "Assembling static components...",
        "Writing blogs/{slug}.html...",
        "Backing up blog.html...",
        "Parsing blog.html structure...",
        "Injecting blog listing cards...",
        "Syncing assets references...",
        "Writing updates to disk...",
        "Done! Post successfully generated! =^.^="
    ]

    # Alternating happy/waving cats for the animation
    save_cats = [LOLCATS[1], LOLCATS[7], LOLCATS[1], LOLCATS[7]]

    for idx, step in enumerate(steps):
        stdscr.erase()
        # Shadow
        for r in range(box_h):
            for c in range(box_w):
                sy, sx = box_y + r + 1, box_x + c + 2
                if 0 <= sy < h and 0 <= sx < w:
                    try:
                        stdscr.addch(sy, sx, " ", curses.A_DIM | curses.color_pair(3))
                    except curses.error:
                        pass

        draw_box(stdscr, box_y, box_x, box_h, box_w,
                 " GENERATING ESSAY ", color_pair=2)

        # Progress bar
        percent = int((idx + 1) / len(steps) * 100)
        bar_w = 32
        filled = int(bar_w * (idx + 1) / len(steps))
        bar = "█" * filled + "░" * (bar_w - filled)
        bar_str = f"[{bar}] {percent}%"
        _safe_addstr(stdscr, box_y + 2, box_x + (box_w - len(bar_str)) // 2,
                     bar_str, curses.color_pair(2) | curses.A_BOLD)

        # Step text
        _safe_addstr(stdscr, box_y + 4, box_x + 3, " " * (box_w - 6))
        _safe_addstr(stdscr, box_y + 4, box_x + max(3, (box_w - len(step)) // 2),
                     step[:box_w - 6], curses.color_pair(3))

        # Celebrating cat (alternates frames)
        cat_art = save_cats[idx % len(save_cats)]
        cat_color = curses.color_pair(2) | curses.A_BOLD if idx == len(steps) - 1 else curses.color_pair(5)
        for li, cl in enumerate(cat_art):
            _safe_addstr(stdscr, box_y + 6 + li, box_x + (box_w - len(cl)) // 2,
                         cl, cat_color)

        stdscr.refresh()
        curses.napms(180)

    stdscr.nodelay(False)
    # Flush input buffer
    stdscr.getch()


# --- CORE TUI EDITOR ---
def curses_main(stdscr):
    # Initialize color palette following terminal capabilities
    curses.start_color()
    curses.use_default_colors()

    if curses.COLORS >= 256:
        # Pair 1: Normal Text
        curses.init_pair(1, -1, -1)
        # Pair 2: Accent — Pastel Coral/Orange
        curses.init_pair(2, 209, -1)
        # Pair 3: Borders/Muted — Pastel Lavender
        curses.init_pair(3, 147, -1)
        # Pair 4: Quotes — Pastel Peach/Yellow
        curses.init_pair(4, 223, -1)
        # Pair 5: Media/Success — Pastel Mint Green
        curses.init_pair(5, 121, -1)
        # Pair 6: Extra — Pastel Sky Blue
        curses.init_pair(6, 153, -1)
    elif curses.COLORS >= 16:
        curses.init_pair(1, -1, -1)
        curses.init_pair(2, 9, -1)    # Bright Red
        curses.init_pair(3, 12, -1)   # Bright Blue
        curses.init_pair(4, 11, -1)   # Bright Yellow
        curses.init_pair(5, 10, -1)   # Bright Green
        curses.init_pair(6, 14, -1)   # Bright Cyan
    else:
        curses.init_pair(1, -1, -1)
        curses.init_pair(2, curses.COLOR_RED, -1)
        curses.init_pair(3, curses.COLOR_CYAN, -1)
        curses.init_pair(4, curses.COLOR_YELLOW, -1)
        curses.init_pair(5, curses.COLOR_GREEN, -1)
        curses.init_pair(6, curses.COLOR_CYAN, -1)

    # --- ANIMATED SPLASH SCREEN ---
    stdscr.nodelay(True)
    splash_cat_idx = 0

    frame = 0
    while frame <= 10:
        draw_splash(stdscr, frame, splash_cat_idx)
        curses.napms(130)
        frame += 1
        stdscr.getch()  # flush inputs

    key_pressed = False
    tick = 10
    while not key_pressed:
        # Rotate cat every 20 ticks
        if tick % 20 == 0:
            splash_cat_idx = (splash_cat_idx + 1) % len(LOLCATS)
        draw_splash(stdscr, tick, splash_cat_idx)
        curses.napms(180)
        tick += 1
        ch = stdscr.getch()
        if ch != -1:
            key_pressed = True

    stdscr.nodelay(False)
    
    # --- STATE VARIABLES ---
    title = ""
    category = "Thoughts"
    excerpt = ""
    blocks = [{'type': 'paragraph', 'text': ''}]
    current_block_idx = 0
    cursor_pos = 0
    scroll_top_line = 0
    autocorrect_enabled = True
    status_msg = ""
    status_msg_ticks = 0
    dirty = False
    # Suggestions state
    suggestions = []
    suggestion_idx = 0
    # Undo-last-autocorrect state
    last_autocorrect_snapshot = None  # (block_idx, old_text, old_cursor_pos)
    
    def trigger_metadata_popup():
        nonlocal title, category, excerpt, dirty

        def draw_bg():
            draw_editor_base(
                stdscr, title, category, excerpt, blocks, current_block_idx,
                cursor_pos, scroll_top_line, autocorrect_enabled, status_msg,
                bg_cat_positions=None, bg_frame=0
            )
        res = edit_metadata_dialog(stdscr, title, category, excerpt, draw_bg)
        if res:
            title, category, excerpt = res
            dirty = True
            return True
        return False

    def draw_editor_base(stdscr, title, category, excerpt, blocks, current_block_idx,
                         cursor_pos, scroll_top_line, autocorrect_enabled, status_msg,
                         bg_cat_positions=None, bg_frame=0,
                         suggestions=None, suggestion_idx=0):
        h, w = stdscr.getmaxyx()

        # Unified single-line outer border (muted lavender)
        draw_box(stdscr, 0, 0, h - 1, w,
                 " MEIN LOUNGE — ESSAY EDITOR v3.0 ", color_pair=3)

        # ---- Metadata bar ----
        title_disp = title if title else "(Untitled Essay)"
        meta_str = (f" {title_disp[:28]} │ {category[:12]} │ {excerpt[:35]}…")
        _safe_addstr(stdscr, 1, 2, " " * (w - 4))
        _safe_addstr(stdscr, 1, 2, meta_str[:w - 4], curses.color_pair(3))

        # Separator rule (single-line, consistent)
        sep = "├" + "─" * (w - 2) + "┤"
        _safe_addstr(stdscr, 2, 0, sep, curses.color_pair(3))

        # ---- Cat corner decorations ----
        # Top-right: tiny cat
        corner_cat = MINI_CATS[bg_frame % len(MINI_CATS)]
        cc_x = max(0, w - len(corner_cat[0]) - 3)
        for li, cl in enumerate(corner_cat):
            _safe_addstr(stdscr, 1 + li, cc_x, cl,
                         curses.color_pair(4) | curses.A_DIM)

        edit_height = h - 6
        edit_width = w - 10

        # ---- Rebuild layout text wraps ----
        wrapped_lines = []
        cursor_global_line = 0
        cursor_col = 0
        line_counter = 0

        for b_idx, block in enumerate(blocks):
            btype = block['type']
            text = block['text']
            lines, positions = wrap_block_text(text, edit_width)

            for l_idx, line_text in enumerate(lines):
                wrapped_lines.append({
                    'block_idx': b_idx,
                    'line_in_block': l_idx,
                    'text': line_text,
                    'type': btype
                })

                if b_idx == current_block_idx:
                    if cursor_pos < len(positions):
                        target_l, target_c = positions[cursor_pos]
                    else:
                        target_l, target_c = positions[-1]
                    if l_idx == target_l:
                        cursor_global_line = line_counter
                        cursor_col = target_c
                line_counter += 1

        # Scroll adjustment
        if cursor_global_line < scroll_top_line:
            scroll_top_line = cursor_global_line
        elif cursor_global_line >= scroll_top_line + edit_height:
            scroll_top_line = cursor_global_line - edit_height + 1

        # ---- Draw editor lines ----
        for screen_row in range(edit_height):
            global_line_idx = scroll_top_line + screen_row
            row_y = 3 + screen_row
            _safe_addstr(stdscr, row_y, 1, " " * (w - 2))

            if global_line_idx < len(wrapped_lines):
                line_data = wrapped_lines[global_line_idx]
                b_idx = line_data['block_idx']
                l_idx = line_data['line_in_block']
                l_text = line_data['text']
                b_type = line_data['type']
                is_active = (b_idx == current_block_idx)

                if l_idx == 0:
                    if b_type == 'heading':
                        lbl, color = " H ", curses.color_pair(2) | curses.A_BOLD
                    elif b_type == 'quote':
                        lbl, color = " Q ", curses.color_pair(4) | curses.A_BOLD
                    elif b_type == 'image':
                        lbl, color = "IMG", curses.color_pair(5) | curses.A_BOLD
                    elif b_type == 'video':
                        lbl, color = "VID", curses.color_pair(5) | curses.A_BOLD
                    elif b_type == 'music':
                        lbl, color = "MUS", curses.color_pair(5) | curses.A_BOLD
                    else:
                        lbl, color = " P ", curses.color_pair(3) | curses.A_BOLD

                    prefix = "▸" if is_active else " "
                    gutter = f"{prefix}{lbl}│ "
                else:
                    gutter = "    │ "
                    color = curses.color_pair(3)

                _safe_addstr(stdscr, row_y, 2, gutter, curses.color_pair(3))
                if l_idx == 0:
                    _safe_addstr(stdscr, row_y, 3, lbl, color)

                # Format block contents
                text_color = curses.color_pair(1)
                if b_type == 'heading':
                    text_color = curses.color_pair(1) | curses.A_BOLD
                elif b_type == 'quote':
                    text_color = curses.color_pair(4) | curses.A_DIM
                elif b_type in ['image', 'video', 'music']:
                    text_color = curses.color_pair(5) | curses.A_DIM

                _safe_addstr(stdscr, row_y, 9, l_text[:edit_width], text_color)

        # ---- Drifting background cats (subtle) ----
        if bg_cat_positions:
            draw_drifting_cats(stdscr, bg_frame, bg_cat_positions)

        # ---- Suggestions bar (above footer) ----
        sugg_row = h - 4
        _safe_addstr(stdscr, sugg_row, 1, " " * (w - 2))
        if suggestions:
            sugg_label = " ◈ "
            _safe_addstr(stdscr, sugg_row, 2, sugg_label, curses.color_pair(6) | curses.A_BOLD)
            sx = 2 + len(sugg_label)
            for si, sw in enumerate(suggestions[:7]):
                if sx >= w - 4:
                    break
                if si == suggestion_idx:
                    attr = curses.color_pair(2) | curses.A_REVERSE | curses.A_BOLD
                else:
                    attr = curses.color_pair(3)
                cell = f" {sw} "
                _safe_addstr(stdscr, sugg_row, sx, cell[:w - sx - 2], attr)
                sx += len(cell)
                if si < len(suggestions) - 1 and sx < w - 4:
                    _safe_addstr(stdscr, sugg_row, sx, " │", curses.color_pair(3))
                    sx += 2
            # Hint
            hint_sugg = "Tab=accept  Ctrl+→/←=cycle"
            _safe_addstr(stdscr, sugg_row, w - len(hint_sugg) - 3,
                         hint_sugg, curses.color_pair(3) | curses.A_DIM)
        else:
            _safe_addstr(stdscr, sugg_row, 2, " " * (w - 4))

        # ---- Footer separator ----
        foot_sep = "├" + "─" * (w - 2) + "┤"
        _safe_addstr(stdscr, h - 3, 0, foot_sep, curses.color_pair(3))

        ac_status = "ON ✓" if autocorrect_enabled else "OFF"
        shortcut_hint = (f"[Ctrl+/] Actions  [Ctrl+S] Save  [Ctrl+Q] Quit  "
                         f"[Ctrl+E] Meta  [Ctrl+A] AC:{ac_status}  [Ctrl+Z] Undo AC")
        _safe_addstr(stdscr, h - 2, 2, shortcut_hint[:w - 4], curses.color_pair(3))

        word_count = sum(len(b['text'].split()) for b in blocks)
        block_hint = f"Blk {current_block_idx + 1}/{len(blocks)} · {word_count}w "
        _safe_addstr(stdscr, h - 2, w - len(block_hint) - 2, block_hint,
                     curses.color_pair(3))

        if status_msg:
            _safe_addstr(stdscr, h - 2, 2, " " * (w - 4))
            _safe_addstr(stdscr, h - 2, 2, f"ℹ {status_msg}"[:w - 4],
                         curses.color_pair(2) | curses.A_BOLD)

        cursor_y = 3 + (cursor_global_line - scroll_top_line)
        cursor_x = 9 + min(cursor_col, edit_width - 1)
        return cursor_y, cursor_x, scroll_top_line

    # Background drifting cats for editor
    h_init, w_init = stdscr.getmaxyx()
    bg_cat_positions = make_cat_positions(h_init, w_init, count=4)
    bg_frame = 0

    # First initialize by asking for Metadata
    trigger_metadata_popup()

    # --- MAIN INPUT LOOP ---
    while True:
        h, w = stdscr.getmaxyx()
        edit_height = h - 6
        edit_width = w - 10
        bg_frame += 1

        # Update suggestions for current partial word
        block_for_sugg = blocks[current_block_idx]
        if block_for_sugg['type'] in ['paragraph', 'heading', 'quote']:
            partial = get_current_partial_word(block_for_sugg['text'], cursor_pos)
            if partial and len(partial) >= 2:
                suggestions = get_suggestions(partial, n=7)
            else:
                suggestions = []
                suggestion_idx = 0
        else:
            suggestions = []
            suggestion_idx = 0

        # Redraw
        cursor_y, cursor_x, scroll_top_line = draw_editor_base(
            stdscr, title, category, excerpt, blocks, current_block_idx,
            cursor_pos, scroll_top_line, autocorrect_enabled, status_msg,
            bg_cat_positions=bg_cat_positions, bg_frame=bg_frame,
            suggestions=suggestions, suggestion_idx=suggestion_idx
        )
        
        # Position terminal cursor
        curses.curs_set(1)
        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        
        try:
            ch = stdscr.get_wch()
        except curses.error:
            continue
            
        # Clear status messages on new input
        if status_msg_ticks > 0:
            status_msg_ticks -= 1
            if status_msg_ticks <= 0:
                status_msg = ""
                
        # --- PROCESS KEYCODES ---
        if is_backspace(ch):
            block = blocks[current_block_idx]
            if cursor_pos > 0:
                block['text'] = block['text'][:cursor_pos-1] + block['text'][cursor_pos:]
                cursor_pos -= 1
                dirty = True
            elif cursor_pos == 0 and current_block_idx > 0:
                # Merge text block with previous text block
                prev_block = blocks[current_block_idx - 1]
                if prev_block['type'] in ['paragraph', 'heading', 'quote'] and block['type'] in ['paragraph', 'heading', 'quote']:
                    old_len = len(prev_block['text'])
                    prev_block['text'] += block['text']
                    blocks.pop(current_block_idx)
                    current_block_idx -= 1
                    cursor_pos = old_len
                    dirty = True
            continue
            
        if isinstance(ch, str):
            code = ord(ch)
            
            # --- CTRL SHORTCUTS ---
            if code == 17: # Ctrl+Q (Quit)
                if dirty:
                    def draw_bg():
                        draw_editor_base(stdscr, title, category, excerpt, blocks, current_block_idx, cursor_pos, scroll_top_line, autocorrect_enabled, status_msg)
                    idx = menu_dialog(stdscr, " QUIT EDITOR? ", ["Quit without saving", "Cancel"], 1, draw_bg)
                    if idx == 0:
                        break
                else:
                    break
                    
            elif code == 19: # Ctrl+S (Save)
                if not title.strip():
                    status_msg = "Error: Title is required before saving."
                    status_msg_ticks = 1
                    trigger_metadata_popup()
                    continue
                    
                # Overwrite confirmation check
                slug = slugify(title)
                file_path = os.path.join(BLOGS_DIR, f"{slug}.html")
                do_save = True
                
                if os.path.exists(file_path):
                    def draw_bg():
                        draw_editor_base(stdscr, title, category, excerpt, blocks, current_block_idx, cursor_pos, scroll_top_line, autocorrect_enabled, status_msg)
                    idx = menu_dialog(
                        stdscr, " OVERWRITE WARNING ", 
                        [f"[y] Overwrite existing {file_path}", "[n] Cancel and rename title"], 
                        0, draw_bg
                    )
                    if idx != 0:
                        do_save = False
                        
                if do_save:
                    # Run generation
                    success, msg = save_blog(title, category, excerpt, blocks)
                    if success:
                        save_animation(stdscr)
                        status_msg = f"Success! Generated {msg}"
                        status_msg_ticks = 2
                        dirty = False
                    else:
                        status_msg = f"Save failed: {msg}"
                        status_msg_ticks = 2
                        
            elif code == 5: # Ctrl+E (Edit Metadata)
                trigger_metadata_popup()
                
            elif code == 1: # Ctrl+A (Toggle Autocorrect)
                autocorrect_enabled = not autocorrect_enabled
                status_msg = f"Autocorrect turned {'ON' if autocorrect_enabled else 'OFF'}"
                status_msg_ticks = 1

            elif code == 26: # Ctrl+Z (Undo last autocorrect)
                if last_autocorrect_snapshot:
                    b_idx, old_txt, old_pos = last_autocorrect_snapshot
                    blocks[b_idx]['text'] = old_txt
                    if b_idx == current_block_idx:
                        cursor_pos = old_pos
                    last_autocorrect_snapshot = None
                    status_msg = "Autocorrect undone."
                    status_msg_ticks = 2
                    dirty = True
                else:
                    status_msg = "Nothing to undo."
                    status_msg_ticks = 1
                
            elif code == 4: # Ctrl+D (Delete Block)
                if len(blocks) > 1:
                    blocks.pop(current_block_idx)
                    current_block_idx = min(current_block_idx, len(blocks) - 1)
                    cursor_pos = 0
                    dirty = True
                    status_msg = "Deleted current block."
                    status_msg_ticks = 1
                else:
                    blocks[0]['text'] = ""
                    cursor_pos = 0
                    dirty = True
                    status_msg = "Cleared content."
                    status_msg_ticks = 1
                    
            elif code == 21: # Ctrl+U (Move Block Up)
                if current_block_idx > 0:
                    blocks[current_block_idx], blocks[current_block_idx - 1] = blocks[current_block_idx - 1], blocks[current_block_idx]
                    current_block_idx -= 1
                    dirty = True
                    status_msg = "Moved block up."
                    status_msg_ticks = 1
                    
            elif code == 14: # Ctrl+N (Move Block Down)
                if current_block_idx < len(blocks) - 1:
                    blocks[current_block_idx], blocks[current_block_idx + 1] = blocks[current_block_idx + 1], blocks[current_block_idx]
                    current_block_idx += 1
                    dirty = True
                    status_msg = "Moved block down."
                    status_msg_ticks = 1
                    
            elif code == 20: # Ctrl+T (Keyboard Help)
                def draw_bg():
                    draw_editor_base(stdscr, title, category, excerpt, blocks, current_block_idx, cursor_pos, scroll_top_line, autocorrect_enabled, status_msg)
                show_help_dialog(stdscr, draw_bg)
                
            elif code in [31, 11, 15]: # Ctrl+/ (31) or Ctrl+K (11) or Ctrl+O (15) for actions menu
                def draw_bg():
                    draw_editor_base(stdscr, title, category, excerpt, blocks, current_block_idx, cursor_pos, scroll_top_line, autocorrect_enabled, status_msg)
                items = [
                    "[p] Change block type to Paragraph",
                    "[h] Change block type to Heading",
                    "[q] Change block type to Quote",
                    "[i] Change block type to Image",
                    "[v] Change block type to Video",
                    "[m] Change block type to Music",
                    "────────────────────────────────────",
                    "[P] Insert Paragraph block below",
                    "[H] Insert Heading block below",
                    "[Q] Insert Quote block below",
                    "[I] Insert Image block below",
                    "[V] Insert Video block below",
                    "[M] Insert Music block below",
                    "────────────────────────────────────",
                    "[D] Delete current block (Ctrl+D)",
                    "[U] Move block Up (Ctrl+U)",
                    "[N] Move block Down (Ctrl+N)",
                    "[E] Edit Metadata (Ctrl+E)",
                    "[A] Toggle Autocorrect (Ctrl+A)",
                    "[T] Keyboard Help (Ctrl+T)",
                    "[S] Save & Compile (Ctrl+S)",
                    "[Q] Quit (Ctrl+Q)"
                ]
                sel = menu_dialog(stdscr, " ACTION PANEL ", items, 0, draw_bg)
                if sel is not None:
                    # Action Mapping
                    if sel == 0: blocks[current_block_idx]['type'] = 'paragraph'
                    elif sel == 1: blocks[current_block_idx]['type'] = 'heading'
                    elif sel == 2: blocks[current_block_idx]['type'] = 'quote'
                    elif sel == 3: # Image
                        src = input_dialog(stdscr, " IMAGE PATH ", "Image URL or Path (relative to blogs/):", "../Assets/", draw_bg)
                        if src:
                            cap = input_dialog(stdscr, " IMAGE CAPTION ", "Image Caption (optional):", "", draw_bg)
                            blocks[current_block_idx]['text'] = f"Src: {src} | Cap: {cap or ''}"
                            blocks[current_block_idx]['type'] = 'image'
                            cursor_pos = len(blocks[current_block_idx]['text'])
                    elif sel == 4: # Video
                        code_iframe = input_dialog(stdscr, " VIDEO EMBED ", "Paste YouTube/Vimeo iframe Embed Code:", "", draw_bg)
                        if code_iframe:
                            blocks[current_block_idx]['text'] = code_iframe
                            blocks[current_block_idx]['type'] = 'video'
                            cursor_pos = len(blocks[current_block_idx]['text'])
                    elif sel == 5: # Music
                        code_iframe = input_dialog(stdscr, " MUSIC EMBED ", "Paste Spotify/SoundCloud iframe Embed Code:", "", draw_bg)
                        if code_iframe:
                            blocks[current_block_idx]['text'] = code_iframe
                            blocks[current_block_idx]['type'] = 'music'
                            cursor_pos = len(blocks[current_block_idx]['text'])
                            
                    elif sel == 7: # Insert Paragraph
                        blocks.insert(current_block_idx + 1, {'type': 'paragraph', 'text': ''})
                        current_block_idx += 1
                        cursor_pos = 0
                    elif sel == 8: # Insert Heading
                        blocks.insert(current_block_idx + 1, {'type': 'heading', 'text': ''})
                        current_block_idx += 1
                        cursor_pos = 0
                    elif sel == 9: # Insert Quote
                        blocks.insert(current_block_idx + 1, {'type': 'quote', 'text': ''})
                        current_block_idx += 1
                        cursor_pos = 0
                    elif sel == 10: # Insert Image
                        src = input_dialog(stdscr, " INSERT IMAGE ", "Image URL or Path:", "../Assets/", draw_bg)
                        if src:
                            cap = input_dialog(stdscr, " INSERT CAPTION ", "Image Caption:", "", draw_bg)
                            blocks.insert(current_block_idx + 1, {'type': 'image', 'text': f"Src: {src} | Cap: {cap or ''}"})
                            current_block_idx += 1
                            cursor_pos = len(blocks[current_block_idx]['text'])
                    elif sel == 11: # Insert Video
                        code_iframe = input_dialog(stdscr, " INSERT VIDEO ", "YouTube/Vimeo Embed Code:", "", draw_bg)
                        if code_iframe:
                            blocks.insert(current_block_idx + 1, {'type': 'video', 'text': code_iframe})
                            current_block_idx += 1
                            cursor_pos = len(blocks[current_block_idx]['text'])
                    elif sel == 12: # Insert Music
                        code_iframe = input_dialog(stdscr, " INSERT MUSIC ", "Spotify/SoundCloud Embed Code:", "", draw_bg)
                        if code_iframe:
                            blocks.insert(current_block_idx + 1, {'type': 'music', 'text': code_iframe})
                            current_block_idx += 1
                            cursor_pos = len(blocks[current_block_idx]['text'])
                            
                    elif sel == 14: # Delete block
                        if len(blocks) > 1:
                            blocks.pop(current_block_idx)
                            current_block_idx = min(current_block_idx, len(blocks) - 1)
                            cursor_pos = 0
                        else:
                            blocks[0]['text'] = ""
                            cursor_pos = 0
                    elif sel == 15: # Move block up
                        if current_block_idx > 0:
                            blocks[current_block_idx], blocks[current_block_idx-1] = blocks[current_block_idx-1], blocks[current_block_idx]
                            current_block_idx -= 1
                    elif sel == 16: # Move block down
                        if current_block_idx < len(blocks) - 1:
                            blocks[current_block_idx], blocks[current_block_idx+1] = blocks[current_block_idx+1], blocks[current_block_idx]
                            current_block_idx += 1
                    elif sel == 17: trigger_metadata_popup()
                    elif sel == 18:
                        autocorrect_enabled = not autocorrect_enabled
                        status_msg = f"Autocorrect turned {'ON' if autocorrect_enabled else 'OFF'}"
                        status_msg_ticks = 1
                    elif sel == 19:
                        show_help_dialog(stdscr, draw_bg)
                    elif sel == 20:
                        # Save
                        if title.strip():
                            success, msg = save_blog(title, category, excerpt, blocks)
                            if success:
                                save_animation(stdscr)
                                status_msg = f"Generated {msg}"
                                status_msg_ticks = 2
                                dirty = False
                            else:
                                status_msg = f"Save failed: {msg}"
                                status_msg_ticks = 2
                        else:
                            status_msg = "Title required to save!"
                            status_msg_ticks = 1
                            trigger_metadata_popup()
                    elif sel == 21: # Quit
                        if dirty:
                            idx_q = menu_dialog(stdscr, " QUIT? ", ["Quit without saving", "Cancel"], 1, draw_bg)
                            if idx_q == 0:
                                break
                        else:
                            break
                    dirty = True
                    
            elif code in [10, 13]: # Enter Key (split line / edit media)
                block = blocks[current_block_idx]
                
                # If editing media block, Enter brings up editing prompts
                if block['type'] in ['image', 'video', 'music']:
                    def draw_bg():
                        draw_editor_base(stdscr, title, category, excerpt, blocks, current_block_idx, cursor_pos, scroll_top_line, autocorrect_enabled, status_msg)
                        
                    if block['type'] == 'image':
                        # Parse existing Src/Cap
                        src_init, cap_init = "../Assets/", ""
                        if "Src:" in block['text']:
                            m_s = re.search(r'Src:\s*(.*?)(?:\s*\|\s*Cap:|$)', block['text'])
                            m_c = re.search(r'Cap:\s*(.*)', block['text'])
                            if m_s: src_init = m_s.group(1).strip()
                            if m_c: cap_init = m_c.group(1).strip()
                        else:
                            src_init = block['text'].strip()
                            
                        src_res = input_dialog(stdscr, " EDIT IMAGE PATH ", "Image file path (relative to blogs/):", src_init, draw_bg)
                        if src_res is not None:
                            cap_res = input_dialog(stdscr, " EDIT IMAGE CAPTION ", "Image Caption (optional):", cap_init, draw_bg)
                            block['text'] = f"Src: {src_res} | Cap: {cap_res or ''}"
                            cursor_pos = len(block['text'])
                            dirty = True
                    else:
                        # Video / Music code iframe
                        code_res = input_dialog(stdscr, f" EDIT {block['type'].upper()} EMBED ", "Paste iframe Embed Code:", block['text'], draw_bg)
                        if code_res is not None:
                            block['text'] = code_res
                            cursor_pos = len(block['text'])
                            dirty = True
                else:
                    # Text blocks: split paragraph
                    left_text = block['text'][:cursor_pos]
                    right_text = block['text'][cursor_pos:]
                    
                    block['text'] = left_text
                    blocks.insert(current_block_idx + 1, {'type': 'paragraph', 'text': right_text})
                    current_block_idx += 1
                    cursor_pos = 0
                    dirty = True
                    
            # --- TAB: Accept first suggestion ---
            elif code == 9:  # Tab
                if suggestions:
                    block = blocks[current_block_idx]
                    partial = get_current_partial_word(block['text'], cursor_pos)
                    chosen = suggestions[suggestion_idx % len(suggestions)]
                    if partial:
                        # Replace partial word with chosen suggestion
                        start = cursor_pos - len(partial)
                        block['text'] = block['text'][:start] + chosen + block['text'][cursor_pos:]
                        cursor_pos = start + len(chosen)
                        dirty = True
                        status_msg = f"Suggestion accepted: \"{chosen}\""
                        status_msg_ticks = 1
                        suggestions = []
                        suggestion_idx = 0

            # --- NORMAL TYPING CHARACTER ---
            elif code >= 32:
                block = blocks[current_block_idx]

                # Check media blocks: don't allow typing carriage breaks but normal edit is allowed
                block['text'] = block['text'][:cursor_pos] + ch + block['text'][cursor_pos:]
                cursor_pos += 1
                dirty = True

                # Trigger autocorrect on spaces
                if ch == ' ':
                    snapshot_text = block['text'][:cursor_pos - 1 - len(get_current_partial_word(block['text'][:cursor_pos-1], cursor_pos-1))]
                    old_text_snap = block['text']
                    old_pos_snap  = cursor_pos - 1
                    new_txt, new_p, correction, was_fuzzy = check_autocorrect(block['text'], cursor_pos, autocorrect_enabled)
                    if correction:
                        # Save undo snapshot before applying
                        last_autocorrect_snapshot = (current_block_idx, old_text_snap, old_pos_snap)
                        block['text'] = new_txt
                        cursor_pos = new_p
                        fuzzy_tag = " ~fuzzy~" if was_fuzzy else ""
                        status_msg = f"Autocorrected{fuzzy_tag}: \"{correction[0]}\" ➔ \"{correction[1]}\"  [Ctrl+Z undo]"
                        status_msg_ticks = 3
                        
        elif isinstance(ch, int):
            block = blocks[current_block_idx]
            text = block['text']

            # --- Ctrl+RIGHT: cycle suggestion forward ---
            if ch == 565 or ch == curses.KEY_SRIGHT:  # Ctrl+Right (terminal-dependent)
                if suggestions:
                    suggestion_idx = (suggestion_idx + 1) % len(suggestions)
                continue

            # --- Ctrl+LEFT: cycle suggestion backward ---
            if ch == 550 or ch == curses.KEY_SLEFT:  # Ctrl+Left (terminal-dependent)
                if suggestions:
                    suggestion_idx = (suggestion_idx - 1) % len(suggestions)
                continue

            # --- ARROW KEY NAVIGATION ---
            if ch == curses.KEY_UP:
                lines, positions = wrap_block_text(text, edit_width)
                if cursor_pos < len(positions):
                    L, col = positions[cursor_pos]
                else:
                    L, col = positions[-1]
                    
                if L > 0:
                    cursor_pos = find_best_cursor_pos(positions, L - 1, col)
                elif current_block_idx > 0:
                    current_block_idx -= 1
                    prev_text = blocks[current_block_idx]['text']
                    prev_lines, prev_positions = wrap_block_text(prev_text, edit_width)
                    prev_last_line = len(prev_lines) - 1
                    cursor_pos = find_best_cursor_pos(prev_positions, prev_last_line, col)
                    
            elif ch == curses.KEY_DOWN:
                lines, positions = wrap_block_text(text, edit_width)
                if cursor_pos < len(positions):
                    L, col = positions[cursor_pos]
                else:
                    L, col = positions[-1]
                    
                if L < len(lines) - 1:
                    cursor_pos = find_best_cursor_pos(positions, L + 1, col)
                elif current_block_idx < len(blocks) - 1:
                    current_block_idx += 1
                    next_text = blocks[current_block_idx]['text']
                    next_lines, next_positions = wrap_block_text(next_text, edit_width)
                    cursor_pos = find_best_cursor_pos(next_positions, 0, col)
                    
            elif ch == curses.KEY_LEFT:
                if cursor_pos > 0:
                    cursor_pos -= 1
                elif current_block_idx > 0:
                    current_block_idx -= 1
                    cursor_pos = len(blocks[current_block_idx]['text'])
                    
            elif ch == curses.KEY_RIGHT:
                if cursor_pos < len(text):
                    cursor_pos += 1
                elif current_block_idx < len(blocks) - 1:
                    current_block_idx += 1
                    cursor_pos = 0
                    
            elif ch == curses.KEY_DC: # Delete key
                if cursor_pos < len(text):
                    block['text'] = block['text'][:cursor_pos] + block['text'][cursor_pos+1:]
                    dirty = True
                    
            elif ch == curses.KEY_RESIZE:
                # Force refresh editor grids
                pass


def main():
    # Verify file template exists
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Error: Template file not found at {TEMPLATE_PATH}. Please verify your directories.")
        sys.exit(1)
        
    try:
        curses.wrapper(curses_main)
    except KeyboardInterrupt:
        pass
    print("\nThank you for using Mein Lounge Typography Editor Suite!\n")

if __name__ == "__main__":
    main()
