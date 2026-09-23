# -*- coding: utf-8 -*-
"""
Content for the CSA Africa website.

Every string here is taken from the live csaafrica.org site. Nothing is
invented: copy has only been re-ordered, split into shorter blocks, or given
headings/labels so it can be laid out editorially.
"""

ORG = "Computer Science Academy Africa"
EMAIL = "csacademyafrica@gmail.com"
FOOTER_ABOUT = ("CSA Africa is based at the School of Computing Science, University of "
                "Glasgow, but our work spans the African continent.")

LINKS = {
    # Must match csaafrica.org exactly. The id is long and was previously
# truncated here, which took applicants to a Microsoft Forms error page.
    "volunteer": "https://forms.office.com/pages/responsepage.aspx?id=KVxybjp2UE-B8i4lTwEzyNYh8sd1qzlKhtxB8q6RSWpUQTZDT05MRVFEWDI0SjYwQURaWVFXRFpDVi4u&route=shorturl",
    "donate": "https://givingtoglasgow.hubbub.net/p/csaafrica/",
    "inuka_apply": "https://docs.google.com/forms/d/e/1FAIpQLScXetmtBR-SeBiHEMyhOAmfimMNN2wO9En8iLJgvNHRMQ36Qw/viewform?usp=dialog",
    "swahilipot": "https://www.swahilipothub.co.ke/",
    "sofiat_gla": "https://www.gla.ac.uk/schools/computing/staff/sofiatolaosebikan/",
    "sofiat_site": "https://www.sofiatolaosebikan.com/",
}

SOCIALS = [
    ("LinkedIn", "https://www.linkedin.com/company/csaafrica/",
     "M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1 4.98 2.12 4.98 3.5zM.22 8.02h4.56V24H.22V8.02zM8.34 8.02h4.37v2.18h.06c.61-1.15 2.1-2.37 4.32-2.37 4.62 0 5.47 3.04 5.47 6.99V24h-4.56v-7.28c0-1.74-.03-3.98-2.43-3.98-2.43 0-2.8 1.9-2.8 3.86V24H8.34V8.02z"),
    ("Instagram", "https://www.instagram.com/csacademyafrica/",
     "M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16zM12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63c-.79.3-1.46.72-2.12 1.38C1.35 2.68.94 3.35.63 4.14.33 4.9.13 5.78.07 7.05.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91.3.79.72 1.46 1.38 2.12.66.66 1.33 1.07 2.12 1.38.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56.79-.3 1.46-.72 2.12-1.38.66-.66 1.07-1.33 1.38-2.12.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91-.3-.79-.72-1.46-1.38-2.12C21.32 1.35 20.65.94 19.86.63 19.1.33 18.22.13 16.95.07 15.67.01 15.26 0 12 0zm0 5.84a6.16 6.16 0 100 12.32A6.16 6.16 0 0012 5.84zm0 10.16a4 4 0 110-8 4 4 0 010 8zm7.85-10.4a1.44 1.44 0 11-2.88 0 1.44 1.44 0 012.88 0z"),
    ("TikTok", "https://www.tiktok.com/@csacademyafrica",
     "M16.6 5.82A4.28 4.28 0 0115.54 3h-3.09v12.4a2.59 2.59 0 01-2.59 2.5 2.59 2.59 0 01-2.59-2.59 2.59 2.59 0 013.19-2.52V9.66a5.7 5.7 0 00-.6-.03A5.68 5.68 0 004.2 15.3 5.68 5.68 0 009.86 21a5.68 5.68 0 005.68-5.68V9.01a7.35 7.35 0 004.3 1.38V7.3a4.28 4.28 0 01-3.24-1.48z"),
    ("YouTube", "https://www.youtube.com/channel/UCXm5CcHVNkjLK9IsHDnKdrA",
     "M23.5 6.19a3.02 3.02 0 00-2.12-2.14C19.5 3.55 12 3.55 12 3.55s-7.5 0-9.38.5A3.02 3.02 0 00.5 6.19C0 8.08 0 12 0 12s0 3.92.5 5.81a3.02 3.02 0 002.12 2.14c1.88.5 9.38.5 9.38.5s7.5 0 9.38-.5a3.02 3.02 0 002.12-2.14C24 15.92 24 12 24 12s0-3.92-.5-5.81zM9.55 15.57V8.43L15.82 12l-6.27 3.57z"),
    ("X", "https://twitter.com/CSAcademyAfrica",
     "M18.24 2.25h3.31l-7.23 8.26 8.5 11.24h-6.66l-5.21-6.82-5.97 6.82H1.66l7.73-8.84L1.25 2.25h6.83l4.71 6.23 5.45-6.23zm-1.16 17.52h1.83L7.08 4.13H5.12l11.96 15.64z"),
    ("Facebook", "https://www.facebook.com/CSAcademyAfrica/",
     "M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.09 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.96h-1.51c-1.49 0-1.96.93-1.96 1.89v2.26h3.33l-.53 3.49h-2.8V24C19.61 23.09 24 18.1 24 12.07z"),
]

# ---------------------------------------------------------------- impact
IMPACT = [
    ("5", None, None, None, "Python programming workshops"),
    ("700", 700, "", "+", "Lives transformed across 13 African countries"),
    ("50", 50, "", "%", "Female participation consistently maintained since 2022"),
    ("90", 90, "", "%", "Participants reported improved programming confidence"),
    ("200k+", None, None, None, "Raised in funding and institutional support"),
]

DIFFERENTIATORS = [
    "Our workshop is free at the point of need",
    "We are intentional about gender parity",
    "We provide childcare support for mothers",
    "We provide accommodation in the host university hostel",
    "We reimburse the cost of road travel for those attending from afar",
    "We run confidence and mindset transformation sessions",
]

TRACKS = [
    "Python Fundamentals (for beginners)",
    "Python for Software Engineering",
    "Python for Data Science",
    "Python for Machine Learning",
    "Python for Internet of Things (IoT)",
]

TIMELINE = [
    ("January / February", "Call for applications opens"),
    ("May", "Selected participants notified"),
    ("July / August", "Workshop takes place"),
]

SUPPORT = [
    ("Accommodation", "Provided for participants traveling from outside the host city"),
    ("Childcare", "On-site support for mothers attending with young children"),
    ("Travel support", "Road transportation covered within regional zones (e.g., West Africa, East Africa)"),
    ("Mentorship", "Ongoing connection with instructors and alumni networks beyond the three weeks"),
]

GAINS = [
    ("Confidence", "Clarity about their next steps in their tech journey"),
    ("Community", "Connections with like-minded peers, potential collaborators, and mentors"),
    ("Practical experience", "A completed project addressing a real-world problem"),
    ("Ongoing support", "Access to alumni networks and continued mentorship"),
]

AFTER_WORKSHOP = [
    "Securing fellowships and scholarships for further study",
    "Landing internships and tech jobs",
    "Winning hackathons and coding competitions",
    "Building solutions that tackle local challenges in health, agriculture, education, and governance",
    "Becoming tutors and mentors for future CSA cohorts",
]

# ---------------------------------------------------------------- editions
# Workshop editions only. There was no 2026 workshop — 2026's event is INUKA
# Mombasa, which lives in its own section and page. A future announced edition
# goes here with slug=None and it renders as a "coming soon" card.
EDITIONS = [
    {"year": "2025", "slug": "csa-2025", "place": "University of Nairobi, Kenya",
     "img": "story/peer-learning", "tag": None, "dates": "14 - 31 July (3 weeks)"},
    {"year": "2022", "slug": "csa-2022", "place": "NitHub, University of Lagos, Nigeria",
     "img": "story/lagos-2022", "tag": None, "dates": "18 July - 03 August (3 weeks)"},
    {"year": "2021", "slug": "csa-2021", "place": "Online (COVID pandemic era)",
     "img": "story/online-2021", "tag": None, "dates": "30 August - 10 September (2 weeks)"},
    {"year": "2019", "slug": "csa-2019", "place": "University of Rwanda, Kigali",
     "img": "story/kigali-2019", "tag": None, "dates": "19 - 30 August (2 weeks)"},
    {"year": "2018", "slug": "csa-2018", "place": "University of Ibadan, Nigeria",
     "img": "story/ibadan-2018", "tag": None, "dates": "30 July - 10 August (2 weeks)"},
]

EDITION_PAGES = {
    "2025": {
        "title": "CSA Africa 2025",
        "place": "University of Nairobi, Kenya",
        "dates": "14 - 31 July (3 weeks)",
        "hero": "story/nairobi-2025",
        "stats": [("200", "Participants selected"), ("51%", "Female"),
                  ("9", "African countries represented"), ("3", "Concurrent learning tracks"),
                  ("14", "Tutors and volunteers"), ("90", "Participants accommodated"),
                  ("40", "Local travel reimbursed"), ("6", "Childcare support for parents")],
        "highlights": [
            "Participants joined us from Kenya, Nigeria, Ghana, Uganda, Rwanda, Tanzania, Eswatini, Cameroon, and Togo.",
            "One mother attended with her three-year-old son — made possible through our on ground childcare support.",
            "Three concurrent learning tracks: Python fundamentals, Python for Software Engineering, and Python for Data Science.",
            "Industry experts shared insights on career opportunities, scholarships, and professional networking at our mini-conference.",
            "Participants reported improved: programming confidence, problem-solving skills, networking, and collaboration abilities.",
        ],
        "video": ("pNHeZ6DvzM8", "video/csa2025-film", "CSA Africa 2025 Workshop Documentary — Highlights & Transformations"),
        "count": 25,
    },
    "2022": {
        "title": "CSA Africa 2022",
        "place": "NitHub, University of Lagos, Nigeria",
        "dates": "18 July - 03 August (3 weeks)",
        "hero": "story/lagos-2022",
        "stats": [("2,024", "Applications received"), ("200", "Participants selected"),
                  ("49%", "Female"), ("4", "Concurrent learning tracks"),
                  ("15", "Tutors and volunteers"), ("126", "Participants accommodated"),
                  ("36", "Local travel reimbursed"), ("4", "Childcare support for parents")],
        "highlights": [
            "Three mothers attended with their children — made possible through our on ground childcare support.",
            "Four concurrent learning tracks: Python fundamentals, Data Structures and Algorithms, Python for Internet of Things, and Introduction to Machine Learning.",
            "Hosted “Breaking the Glass Ceiling” mini-conference featuring 4 Nigerian women in tech. This conference also included an anonymous barrier-sharing session revealing systemic challenges, as well as a kindness session where attendees wrote encouraging notes to one another.",
            "Participants reported improved programming confidence and problem-solving skills.",
            "Participants built several projects including medical bots, ML crop advisors, and IoT simulations.",
        ],
        "video": None,
        "count": 25,
    },
    "2021": {
        "title": "CSA Africa 2021",
        "place": "Online (COVID pandemic era)",
        "dates": "30 August - 10 September (2 weeks)",
        "hero": "story/online-2021",
        "stats": [("487", "Applications received"), ("172", "Participants selected"),
                  ("16%", "Female"), ("3", "Concurrent learning tracks"),
                  ("50", "Tutors and volunteers"), ("120", "Received internet provision")],
        "highlights": [
            "First fully online workshop delivered via Zoom and Gather Town, with 40 volunteers supporting participants in virtual hands-on sessions.",
            "Three concurrent learning tracks: Python fundamentals, Data Structures and Algorithms, and Python for Machine Learning.",
            "Provided 40GB of data to participants facing connectivity issues, ensuring internet access wouldn’t block learning.",
            "Despite internet outages, power cuts, and the challenge of building confidence online, 80% of participants completed daily coding tasks.",
            "One mother completed coding tasks with her daughter “shouting in her ear sometimes” — tutors celebrated her determination.",
            "Participants built book recommender systems, Spotify data visualisations, and family-tree implementations as final projects.",
        ],
        "video": None,
        "count": 6,
    },
    "2019": {
        "title": "CSA Africa 2019",
        "place": "University of Rwanda, Kigali",
        "dates": "19 - 30 August (2 weeks)",
        "hero": "story/kigali-2019",
        "stats": [("100", "Participants selected"), ("15%", "Female"),
                  ("2", "Concurrent learning tracks"), ("7", "Tutors and volunteers")],
        "highlights": [
            "The workshop’s impact led the University of Rwanda to incorporate Python programming into their official curriculum.",
            "One participant travelled 25 hours by road from Kenya to attend — many juggled work and family commitments to participate.",
            "Two CSA 2018 alumni (Ifeoma and Paul from University of Ibadan) returned as tutors, building capacity to organise future workshops.",
            "Participants split into two experience-based groups, covering everything from basic programming to data analysis, BBC micro:bit, and object-oriented Python.",
            "Teams built an interpreter and tackled data science challenges, presenting their work on the final day.",
            "Participants gained remarkable confidence over two weeks, explaining concepts to peers and tackling errors independently.",
        ],
        "video": None,
        "count": 25,
    },
    "2018": {
        "title": "CSA Africa 2018",
        "place": "University of Ibadan, Nigeria",
        "dates": "30 July - 10 August (2 weeks)",
        "hero": "story/ibadan-2018",
        "stats": [("120", "Participants selected"), ("17%", "Female"), ("5", "Tutors and volunteers")],
        "highlights": [],
        "video": None,
        "count": 25,
    },
}

# ---------------------------------------------------------------- testimonials
TESTIMONIALS = [
    ("Marcella Barasa", "CSA Africa 2025", "people/marcella-barasa",
     "Bringing my 3-year-old son to CSA’s workshop changed everything, thanks to their childcare "
     "support. It proved nothing is impossible. When challenges come, I remember: I was selected, I "
     "travelled to Nairobi, I did this. Now girls in my community see me and know it’s never too "
     "late to take chances on themselves."),
    ("Phenny Mwaisaka", "CSA Africa 2025", "people/phenny-mwaisaka",
     "My team and I won $1,000 at the UNEP hackathon and now we’re piloting our project with KEFRI. "
     "CSA gave me the confidence to compete and unlocked a chain reaction: from joining the data "
     "community to discovering a passion that shapes my career every day."),
    ("Abiodun Allison", "CSA Africa 2018", "people/abiodun-allison",
     "CSA 2018 bridged math theory and real engineering for me, launching everything that followed: "
     "neural network research, my ML Engineer intern role, to building OCR systems that transform "
     "handwritten books into digital ledgers. Now I’m paying it forward as Lead Tutor for Data "
     "Science Nigeria, teaching 80+ students what CSA taught me."),
    ("Osborn Nyakaru", "CSA Africa 2025", "people/osborn-nyakaru",
     "Before CSA, I looked for assignments to complete. After, I looked for problems to solve. That "
     "shift led me to build a platform connecting users to hackathons, turning the skills we learn "
     "into real-world solutions. CSA didn’t just teach me to code; it taught me to see "
     "opportunities everywhere."),
    ("Carren Green", "CSA Africa 2025", "people/carren-green",
     "CSA ended my confusion about which tech path to choose, even as a computing student. The "
     "workshop gave me clarity and skills I could use immediately. Now I’m analysing health "
     "datasets a Kenyan company trusted me with, contributing to real decision-making."),
    ("Ireoluwa Olutunmibi", "CSA Africa 2022", "people/ireoluwa-olutunmibi",
     "CSA changed my mindset from passive acceptance to active problem-solving. I thought of a "
     "solution to every problem I encountered and sought out opportunities: I got a part-time job "
     "teaching robotics to elementary school pupils, multiple paid internship opportunities, even "
     "won a MacBook."),
    ("Paul Njoroge", "CSA Africa 2025", "people/paul-njoroge",
     "After losing my only parent, I was drowning in depression with no hope. CSA ignited my passion "
     "for programming and gave me a reason to keep going. Now I’m building tools, writing again, "
     "and planning to return to school. This workshop literally saved my life."),
    ("Usman Akinyemi", "CSA Africa 2022", "people/usman-akinyemi",
     "The CSA Africa workshop is the best in-person programming bootcamp I’ve ever attended in "
     "Nigeria. It significantly strengthened my Python skills and deepened my understanding of core "
     "computer science concepts—making my current undergraduate CS coursework much easier to "
     "grasp. The experience also opened real-world opportunities: I completed my first internship "
     "working on a Python-based project and even contributed to the official Python documentation."),
    ("Deborah Oluwabunmi Joseph", "CSA Africa 2018", "people/deborah-joseph",
     "Before the program, I had little knowledge of programming and with a great desire to know more. "
     "Today, I am proficient in Python, Kotlin, and C++ programming languages, and work as a Mobile "
     "Software Engineer. The CSA Africa initiative gave me the solid foundation in which I have built "
     "all my technical skills on."),
    ("Halimat Amzat", "CSA Africa 2022", "people/halimat-amzat",
     "CSA Africa transformed my journey from a physics student with no coding background into a "
     "confident programmer and leader. It helped me excel in CS courses, earn a scholarship, join the "
     "Ghana Data Science Bootcamp, and get elected as Vice President of my department. I even built a "
     "GPA calculator to support my peers, proof of how practical and empowering the experience was."),
    ("Taoheed Popoola", "CSA Africa 2025", "people/taoheed-popoola",
     "Three months after graduation, I’m interning at a major fintech company in Nigeria and I’m "
     "still emotional about it. CSA gave me what coursework couldn’t: real confidence, hands-on "
     "skills, and proof that I belong in tech."),
    ("Motunrayo Sanyaolu", "CSA Africa 2022", "people/motunrayo-sanyaolu",
     "CSA Africa helped me find my direction. I was initially unsure of my path, but by the end of the "
     "workshop, I confidently chose to pursue the Internet of Things (IoT). I connected with brilliant "
     "peers who supported my growth, and the knowledge I gained has empowered me to innovate and "
     "ultimately led to my role as an IoT Ecosystem Lead."),
    ("Keside Onyeocha", "CSA Africa 2022", "people/keside-onyeocha",
     "The CSA Africa initiative has left an indelible mark on my life, enriching me with invaluable "
     "skills and fostering lifelong connections. Immersed in the Internet of Things (IoT) track, I "
     "absorbed fundamental concepts and industry knowledge under the guidance of an exceptional tutor."),
    ("Ebele Dafe", "CSA Africa 2022", "people/ebele-dafe",
     "The CSA Africa workshop gave me the opportunity to learn new skills, apply Python programming in "
     "my research and improve my coding skills. It has also helped me to connect with other tech "
     "enthusiasts and build a strong professional network."),
]

# ---------------------------------------------------------------- people
LEADERSHIP = [
    ("Dr Sofiat Olaosebikan", "Founder and Lead", "University of Glasgow",
     "team/sofiat-olaosebikan", "https://www.linkedin.com/in/sofiatolaosebikan/"),
    ("Fionnuala Johnson", "Python Fundamentals Lead", "University of Glasgow",
     "team/fionnuala-johnson", "https://www.linkedin.com/in/fionnuala-johnson-b9b84b189/"),
    ("Dr Stephen McQuistin", "Software Engineering Lead", "University of St Andrews",
     "team/stephen-mcquistin", "https://www.linkedin.com/in/smcquistin/"),
    ("Dr Kenechi Omeke", "Python for Data Science Lead", "UK’s ONS",
     "team/kenechi-omeke", "https://www.linkedin.com/in/kenomeke/"),
    ("Dr Peace Ayegba", "Project coordinator", "University of Glasgow",
     "team/peace-ayegba", "https://www.linkedin.com/in/peace-ayegba/"),
]

VOLUNTEERS = [
    ("Dr Fatma Elsafoury", "Python Instructor (2018)", "team/fatma-elsafoury",
     "https://www.linkedin.com/in/dr-fatma-elsafoury-159061291/"),
    ("Dr Benjamin Bumpus", "Python Instructor (2018 - 2019)", "team/benjamin-bumpus",
     "https://bmbumpus.com/about-me/"),
    ("Dr Tom Wallis", "Python Instructor (2018 - 2019)", "team/tom-wallis",
     "https://www.linkedin.com/in/probablytom/"),
    ("Dr Alex Pancheva", "Python Instructor (2019 - 2022)", "team/alex-pancheva",
     "https://www.linkedin.com/in/alexandrina-pancheva-125b00121/"),
    ("Dr Charlie Rex", "Media Volunteer (2022)", "team/charlie-rex",
     "https://www.linkedin.com/in/charlie-rex-phd/"),
    ("Yusuf Sani", "Tutor (2022)", "team/yusuf-sani",
     "https://www.linkedin.com/in/yusuf-abdulaziz-sani/"),
    ("Sarima Chiorlu", "Tutor (2022)", "team/sarima-chiorlu",
     "https://www.linkedin.com/in/sarima-chiorlu-8965b21a1/"),
    ("Israel Odejo", "Tutor (2022)", "team/israel-odejo",
     "https://www.linkedin.com/in/odeajo-israel/"),
    ("Peter Ohue", "Tutor (2022)", "team/peter-ohue",
     "https://www.linkedin.com/in/peter-ohue-42013946/"),
    ("Musa Aka’aba", "Tutor (2022)", "team/musa-akaaba",
     "https://www.linkedin.com/in/akaabamusaakidi/"),
    ("Abduljaleel Adejumo", "Tutor (2022)", "team/abduljaleel-adejumo",
     "https://www.linkedin.com/in/abduljaleel-adejumo/"),
    ("AbdulSamad Abduljaleel", "Tutor (2022)", "team/abdulsamad-abduljaleel",
     "https://www.linkedin.com/in/abdul-samad-abdul-jaleel/"),
    ("Orla Johnson", "Tutor (2025)", "team/orla-johnson",
     "https://www.linkedin.com/in/orla-johnson-102703236/"),
    ("Elkanah Nyabuto", "Tutor (2025)", "team/elkanah-nyabuto",
     "https://www.linkedin.com/in/elkanahnyabuto/"),
    ("Ariane Chrisko", "Tutor (2025)", "team/ariane-chrisko",
     "https://www.linkedin.com/in/ariane-nidelle-meli-chrisko/"),
    ("Grace Wangui", "Tutor (2025)", "team/grace-wangui",
     "https://www.linkedin.com/in/grace-wangui-274504155/"),
    ("Lasisi Romoke", "Tutor (2025)", "team/lasisi-romoke",
     "https://www.linkedin.com/in/romoke-lasisi/"),
    ("Anita Terry", "Tutor (2025)", "team/anita-terry",
     "https://www.linkedin.com/in/terry-anita/"),
    ("Shidmah Orero", "Tutor (2025)", "team/shidmah-orero",
     "https://www.linkedin.com/in/akeyoorero/"),
    ("Edwin Mukhalisi", "Tutor (2025)", "team/edwin-mukhalisi",
     "https://www.linkedin.com/in/mukhalisi-edwin-34508210b/"),
    ("Edith Naike", "Tutor (2025)", "team/edith-naike",
     "https://www.linkedin.com/in/edith-edward-126925239/"),
    ("Lukorito Wepukhulu", "Tutor (2025)", "team/lukorito-wepukhulu",
     "https://www.linkedin.com/in/lukorito-melvin-wepukhulu-89a7a7269/"),
]

# ---------------------------------------------------------------- partners
PARTNERS = [
    ("University of Glasgow", "partners/uni-glasgow"),
    ("University of Nairobi", "partners/uni-nairobi"),
    ("University of Lagos", "partners/uni-lagos"),
    ("University of Rwanda", "partners/uni-rwanda"),
    ("University of Ibadan", "partners/uni-ibadan"),
    ("University of St Andrews", "partners/uni-st-andrews"),
    ("SICSA", "partners/sicsa"),
    ("GCRF", "partners/gcrf"),
    ("Morgan Stanley", "partners/morgan-stanley"),
    ("RS Roots", "partners/rs-roots"),
    ("Trilite", "partners/trilite"),
]

# ---------------------------------------------------------------- news
# (title, image, excerpt, source url, local copy | None)
# The four newspaper pieces are PDFs. We serve our own copies from
# assets/docs/ so they keep working if the original host goes away - three of
# them sit on the old Wix CDN.
NEWS = [
    ("University of Glasgow News", "news/glasgow-news",
     "This article highlights Dr Sofiat Olaosebikan and her initiative (CSA Africa) at the University "
     "of Glasgow, using maths and computing skills to train young scientists across Africa.",
     "https://www.gla.ac.uk/news/archiveofnews/2019/september/headline_673552_en.html", None),
    ("London Mathematical Society Newsletter", "news/lms-newsletter",
     "In this LMS Newsletter (page 31-32), Dr Benjamin Bumpus provides insight on his experience of "
     "teaching programming at the first CSA Africa 2018 workshop.",
     "https://www.lms.ac.uk/sites/lms.ac.uk/files/files/NLMS_481_for%20web.pdf",
     "docs/lms-newsletter-481.pdf"),
    ("TechCabal", "news/techcabal",
     "This article features a CSA Africa participant, Motunrayo Sanyaolu, and how she is using "
     "knowledge gained from our Python workshop to innovate and create impact.",
     "https://techcabal.com/2025/03/12/unilag-motunrayo-sanyaolu-engineering/", None),
    ("Metro Newspaper", "news/metro",
     "This article profiles Dr Sofiat’s initiatives to introduce thousands of African youths to "
     "Python programming, sparking interest in tech careers and expanding opportunities in STEM.",
     "https://bb716663-aee6-4233-bcad-e44861f5367c.filesusr.com/ugd/303cbb_4cbc45be841c44a8b78db94bf15b3211.pdf",
     "docs/metro-newspaper.pdf"),
    ("QS Top Universities", "news/qs-top-universities",
     "An in-depth Q&A that covers Dr Olaosebikan’s journey from Nigeria to Glasgow and her "
     "mission with CSA Africa.",
     "https://www.topuniversities.com/student-info/student-stories/qa-future-world-changer-sofiat-olaosebikan", None),
    ("The Herald Newspaper", "news/herald",
     "A feature highlighting Dr Sofiat Olaosebikan’s mission to empower young Africans through "
     "computing education.",
     "https://bb716663-aee6-4233-bcad-e44861f5367c.filesusr.com/ugd/303cbb_298c03f80a924a3b8117b1a5e4905ffd.pdf",
     "docs/the-herald.pdf"),
    ("The National Newspaper", "news/the-national",
     "A coverage of Dr Sofiat’s early work training young African scientists, demonstrating how her "
     "academic journey in Scotland fuels impactful grassroots education across the continent.",
     "https://bb716663-aee6-4233-bcad-e44861f5367c.filesusr.com/ugd/303cbb_2c228512d895428faee0b76ddfe37ec1.pdf",
     "docs/the-national.pdf"),
]

# ---------------------------------------------------------------- alumni films
ALUMNI_FILMS = [
    ("KntnVf5wsS8", "video/alumni-1", "Keside’s Journey: How CSA Opened Doors to Success"),
    ("nh_WcUscYQs", "video/alumni-2", "CSA Africa Alumni Interview: Motunrayo Sanyaolu"),
    ("JZ54RXQlE38", "video/alumni-3", "How CSA Changed My Life — Dewa’s Story"),
]

# ---------------------------------------------------------------- INUKA
INUKA = {
    "title": "INUKA Mombasa",
    "tagline": "A mindset transformation experience.",
    "partners": "In partnership with NAA’M Initiative and Swahilipot Hub Foundation",
    "venue": "Swahilipot Hub Foundation, Mombasa",
    "dates": "10 - 13 September (4 days)",
    "close": "Friday 28 August 2026",
    # Flip back to True (and put the copy below into the future tense) when a
    # new call opens. build.py reads this to decide whether the apply CTA is a
    # live link or an inert "Applications closed" label.
    "applications_open": False,
    "spots": "60 spots only",
    "why": [
        "For eight years, CSA Africa has taught young Africans to code. Along the way, we noticed "
        "something no curriculum fixes: talented young people holding back from a belief that people "
        "like them don’t belong in the room. So this year, for the first time, we’re running "
        "something different.",
        "INUKA Mombasa is CSA Africa’s first mindset transformation event. This is for you whether "
        "you are interested in tech, creative arts, media, and so on. No coding experience or "
        "technical background required, just a willingness to challenge what you believe is possible "
        "for your life.",
    ],
    "beyond": [
        "Access to opportunity was never only about skills, it was about belief. About seeing what’s "
        "possible. About someone showing up in your corner before you showed up for yourself.",
        "INUKA Mombasa proves that mindset transformation matters just as much as learning to code, "
        "because without the first, the second rarely sticks.",
    ],
    "walkaway": [
        "A clear, personal answer to “what’s actually possible for me”",
        "Real relationships with mentors and peers who hold you accountable",
        "Something tangible you built yourself",
        "One courageous next step already in motion, and a community behind it",
    ],
    "walkaway_note": "This is four days of real work on your mindset, your confidence, and your next "
                     "move in life and career.",
    "speakers": [
        ("Dr Sofiat Olaosebikan",
         "Lecturer in Computing Science, University of Glasgow, and Founder of CSA Africa",
         "Sofiat applied to study Computer Science three times as an undergraduate applicant and "
         "failed three times. She grew up in an underserved neighbourhood in Lagos with no one to "
         "guide her into a career in tech, and today lectures in the very subject she once "
         "couldn’t get admitted to study. She’ll share exactly how she got from there to here.",
         LINKS["sofiat_site"]),
        ("Nadia Abdalla",
         "Founder of the NAA’M Initiative and a former Chief Administrative Secretary in the "
         "Government of Kenya",
         "Long before she held that title, Nadia was a product of Swahilipot Hub herself, proof that "
         "the room you grow up in can become the room you go on to lead. She’ll share what it took "
         "to go from being someone the system supported to someone shaping the system.",
         None),
    ],
    "also": "You’ll also meet alumni from CSA Africa’s past programmes, young women who walked "
            "into our programme with the same doubts you might be carrying, and walked out doing "
            "things they didn’t think were possible for them. And you’ll be hosted at "
            "Swahilipot Hub, Mombasa’s own home for youth innovation, alongside its mentors and "
            "community.",
    "wait": [
        "Spaces were capped at 60 with 50% reserved for women. Applications closed on Friday "
        "28 August 2026.",
        "Selection was competitive and included a short video. Everyone who applied will hear "
        "from the CSA Africa team directly.",
        "This programme is completely free to attend.",
        "Lunch is provided.",
        "All we ask is your full presence for four days, no exceptions.",
    ],
}

# ------------------------------------------------- INUKA Mombasa 2026 edition
# The event as it happened, 10-13 September 2026. Kept separate from INUKA
# above, which holds the programme-level copy, so a future edition can be
# announced without disturbing this record.
#
# Bios are the organisers' own, from the printed programme booklet. Nothing
# here is paraphrased or invented.
INUKA_2026 = {
    "held": "10 &#8211; 13 September 2026",
    "motto": "Believe. See. Build. Rise.",
}

# (name, role, bio, session)
# session: "mc" | "featured" | "panel-1" | "panel-2" | None
# None means they led a session on days 3-4 that is not yet documented here.
INUKA_PEOPLE = [
    ("Maham Hussein",
     "Communications and Public Affairs Professional",
     "Maham Hussein is a Communications and Public Affairs professional working at the "
     "intersection of strategic communication, international relations and social impact. Her "
     "experience spans institutional storytelling, executive communications, public engagement "
     "and navigating diverse stakeholder spaces across Kenya and Africa. She is particularly "
     "interested in how African institutions tell their own stories, how young people participate "
     "in shaping the continent’s future, and how meaningful conversations can become meaningful "
     "action. When she is not behind the communications strategy, Maham enjoys bringing people, "
     "ideas and energy together (both on and off the stage).",
     "mc"),

    ("Dr Sofiat Olaosebikan",
     "Founder, CSA Africa &#183; Computing Science Lecturer, University of Glasgow",
     "Dr Sofiat Olaosebikan is a Computing Science lecturer at the University of Glasgow and the "
     "Founder of CSA Africa, an initiative focused on expanding access to technology, computing "
     "education and practical digital skills for young Africans. Through CSA Africa, she has "
     "supported the training of more than 700 young Africans across 13 countries, helping "
     "participants build confidence, technical capability and pathways into technology and "
     "innovation. Her own journey into computing was shaped by persistence after repeated "
     "rejection from Computing Science, an experience that now informs her commitment to helping "
     "young people see beyond their circumstances, reframe setbacks and recognise the "
     "possibilities available to them. She is also an Elevate Africa Fellow and is passionate "
     "about technology, education, mentorship and creating practical opportunities for Africa’s "
     "next generation.",
     "featured"),

    ("Dr Swalhah Yusuf, OGW",
     "Deputy Director, Election Operations, Mombasa County &#183; Electoral Management Professional",
     "Dr Swalhah Yusuf, OGW is an electoral management professional with over 14 years of "
     "experience in election operations. She currently serves as the Deputy Director, Election "
     "Operations in Mombasa County, where she oversees the planning and implementation of "
     "electoral activities. She holds a PhD in Business Management, a Master of Business "
     "Administration (Finance), a Bachelor of Commerce (Finance), and is a Certified Public "
     "Accountant of Kenya (CPA-K). Her expertise spans strategic leadership, financial "
     "management, governance, electoral administration and institutional service delivery. "
     "Through her leadership, IEBC has consistently been ranked as the best Independent "
     "Commission at international exhibitions in Mombasa. Dr Yusuf is committed to professional "
     "excellence, institutional integrity, effective service delivery and credible electoral "
     "processes. Her contribution to public service has been recognised through the Order of the "
     "Grand Warrior (OGW) award.",
     "featured"),

    ("Melvine Tabitha Opondo",
     "Computer Science Student &#183; Technologist &#183; CSA Africa Alumna",
     "Melvine Tabitha Opondo is a Computer Science student, technologist and CSA Africa alumna "
     "whose journey is defined by resilience, courage and learning to create opportunities from "
     "where she is. She began university with almost no prior exposure to computers and initially "
     "struggled with feelings of being behind and not belonging in technology. Through "
     "persistence, mentorship and her experience with CSA Africa, she developed skills in "
     "software development while gaining the confidence to approach challenges as things she "
     "could learn rather than limitations on what she could become. Today, Melvine builds "
     "software, works collaboratively on projects and uses her skills to identify problems and "
     "create practical solutions. Her story reflects a belief that lack of exposure is not lack "
     "of ability, and that young people can begin building meaningful opportunities with what "
     "they already have.",
     "panel-1"),

    ("Aseef Akram",
     "Employer Engagement Associate, Global Opportunity Youth Network &#183; Youth &amp; Sports "
     "Development Leader",
     "Aseef Akram is an Employer Engagement Associate at the Global Opportunity Youth Network "
     "(GOYN), working at the intersection of youth employment, skills development and opportunity "
     "creation. He helps bridge the gap between emerging talent and the evolving workforce by "
     "preparing young people for placement, retention and entrepreneurship, while supporting "
     "employers to better recognise and value youth potential. Beyond his work in youth "
     "employment, Aseef serves as Chairman of Blue Ocean Swimming Club and Technical Director at "
     "the Mombasa County Swimming Association, where he supports youth leadership, talent "
     "development and pathways in sport. His work is driven by a commitment to helping young "
     "people access meaningful opportunities, develop their potential and build sustainable "
     "pathways for growth.",
     "panel-1"),

    ("Fatuma Ali",
     "Founder &amp; CEO, Sulha Afrika &#183; Social Entrepreneur &amp; Engineer",
     "Fatuma Ali is an award-winning social entrepreneur, petroleum and natural gas engineer, and "
     "the Founder &amp; CEO of Sulha Afrika, a regenerative materials company developing "
     "mangrove-based biomaterials to transform the leather industry through Indigenous African "
     "knowledge and circular innovation. She founded Sulha Afrika with just USD 300, growing it "
     "from a sustainable leather brand into a pioneering venture advancing nature-based "
     "alternatives to chromium tanning. Her work focuses on developing mangrove-derived "
     "bio-tannins, while creating economic opportunities for women and youth and supporting "
     "ecosystem restoration through regenerative value chains. Fatuma’s work has received "
     "international recognition, including the African Development Bank Fashionomics Africa "
     "Award, the African Union Commission and UNDP Blue Economy Innovation Award, and the EU "
     "BlueInvest Africa Award. She has also presented research on Indigenous African leather "
     "practices at the 126th Society of Leather Technologists and Chemists Annual Conference in "
     "the United Kingdom. Her vision is to position Africa as a global leader in regenerative "
     "material innovation, transforming Indigenous knowledge into scalable climate technologies "
     "that restore biodiversity, strengthen local economies and redefine sustainable "
     "manufacturing.",
     "panel-1"),

    ("Haytam Isse Abdullahi",
     "Founder &amp; Executive Director, Future Pillars Organization &#183; Founder, Guiding the "
     "Lights Leadership Academy",
     "Haytam Isse Abdullahi is a youth leader and social-impact practitioner focused on "
     "leadership development, community empowerment and good governance. He is the Founder and "
     "Executive Director of Future Pillars Organization, a Mombasa-based youth-led organisation, "
     "and the Founder of the Guiding the Lights Leadership Academy, which develops young leaders "
     "through values-based leadership, civic responsibility, integrity and personal development. "
     "His work spans youth mentorship, education, community initiatives and leadership "
     "development, creating platforms that enable young people to lead and contribute "
     "meaningfully to society.",
     "panel-1"),

    ("Kauthar Mohamed",
     "Student Leadership Development Manager &#183; Leadership Architect &amp; Sustainable "
     "Service-Learning Practitioner",
     "Kauthar Mohamed is a youth leadership and education practitioner with over a decade of "
     "experience empowering young people to discover their potential, develop their voice and "
     "turn ideas into meaningful action. As Student Leadership Development Manager at Aga Khan "
     "Academy Mombasa, she leads programmes spanning Service Learning and Community-Based Service "
     "Learning, youth leadership, internships and experiential learning, creating opportunities "
     "for young people to connect learning with purpose, possibility and impact. An International "
     "Baccalaureate alumna herself, Kauthar brings both personal and professional insight into "
     "the transformative power of education and the importance of creating spaces where young "
     "people can see possibilities beyond their immediate circumstances. Passionate about "
     "holistic youth empowerment, authentic leadership and creating pathways to opportunity, "
     "Kauthar is particularly interested in helping young people recognise their value, "
     "communicate their strengths and have the confidence to take up space. Born and raised in "
     "Mombasa, she remains deeply committed to creating opportunities for young people in her "
     "community and beyond. Her personal philosophy, &#8220;Inspire to Empower,&#8221; reflects "
     "her belief that when people are given the confidence, tools and opportunities to see what "
     "is possible, they can begin to build it.",
     "panel-2"),

    ("Edwin Njuga",
     "Development Professional &#183; Youth Empowerment &amp; Enterprise Development Specialist",
     "Edwin Njuga is a development professional with over 20 years of experience across the NGO "
     "and public sectors, including World Vision Kenya, the Department of Children Services, and "
     "the Coast Water Works Development Agency. He has 15 years of experience in youth "
     "empowerment, monitoring and evaluation, enterprise development, and programme coordination. "
     "He has worked with the Youth Enterprise Development Fund (YEDF) in various capacities, "
     "including Monitoring &amp; Evaluation Officer, Regional Coordinator, and County "
     "Coordinator. Throughout his career, he has supported youth-focused programmes, coordinated "
     "field operations, monitored programme performance, facilitated enterprise development "
     "initiatives, and provided technical support to young people and Micro, Small and Medium "
     "Enterprises (MSMEs). Edwin holds a Master’s Degree in Sociology (Rural Sociology and "
     "Community Development), a Bachelor’s Degree in Sociology, and a Diploma in Project Planning "
     "and Management. He is passionate about youth empowerment, entrepreneurship development, and "
     "creating sustainable opportunities for young people.",
     "panel-2"),

    ("Abdulkadir Aweis (Dadir)",
     "Founder, Siewa Media Agency &amp; Siewa Network &#183; Creative Entrepreneur",
     "Abdulkadir Aweis, also known as Dadir, is a creative entrepreneur and the Founder of Siewa "
     "Media Agency and Siewa Network. Through Siewa Media, he works across digital storytelling, "
     "creative media, marketing and strategic communication, helping brands and organisations "
     "strengthen their digital presence, engage relevant audiences and communicate their value "
     "clearly. Siewa Network brings together changemakers, ideas and opportunities across the "
     "creative, business and community sectors, creating a platform for collaboration around "
     "youth empowerment, education, community development and social impact. With over six years "
     "of experience in digital communication and creative work, Dadir has worked with "
     "organisations, businesses, creators and community-led initiatives to build partnerships, "
     "amplify humanitarian campaigns, empower communities and mobilise people and resources "
     "around shared objectives. He is driven by a belief in the power of people, ideas and "
     "meaningful connections to open doors and create new possibilities.",
     "panel-2"),

    # Led sessions on days 3-4. Session details not yet supplied, so they carry
    # no session key and render under the general speaker roster.
    ("Nadia Abdalla",
     "Founder &amp; Executive Director, NAA’M Initiative &#183; Governance, Public Affairs &amp; "
     "Political Advisor &#183; Author",
     "Nadia Abdalla is a Pan-African governance and leadership practitioner, speaker, author, and "
     "the Founder and Executive Director of the NAA’M Initiative &#8212; a platform advancing "
     "mindset transformation, civic participation, future skills and economic empowerment among "
     "women and young people. She previously served as Chief Administrative Secretary (Deputy "
     "Minister) in Kenya’s Ministry of ICT, Innovation and Youth Affairs, a deputy "
     "minister-level government position to which she was appointed at the age of 29. During her "
     "tenure, she advised senior government leadership and championed national initiatives in "
     "youth development, employment, innovation, digital skills and public participation. Nadia "
     "brings experience spanning government, public policy, strategic partnerships, philanthropy, "
     "civil society, international development and the private sector. Her facilitation approach "
     "combines personal storytelling, guided reflection, practical tools and action-based "
     "learning, enabling participants to connect leadership concepts with their everyday "
     "realities. She facilitates sessions on mindset transformation, authentic leadership, civic "
     "responsibility, personal positioning, strategic communication, women and youth leadership, "
     "and navigating personal and professional transitions. Nadia is a three-time author. Through "
     "her work, she equips participants to challenge limiting beliefs, recognise their agency, "
     "communicate their value and take courageous action toward building meaningful futures and "
     "transforming their communities.",
     None),

    ("Dr Hafidha Ahmed",
     "Mental Health Specialist &amp; Community Developer",
     "Dr Hafidha Ahmed is a Mental Health Specialist and Community Developer who supports "
     "individuals in realising their full potential through accessible mental health support and "
     "comprehensive personal development programmes. With extensive experience in the contact "
     "centre industry, she has developed strong skills in leadership, communication and training, "
     "which continue to shape her impact-driven work. She is deeply committed to community "
     "service, public speaking and creating safe spaces that encourage growth, healing and "
     "empowerment. Through CSR and community-centred initiatives, including work around GBV, "
     "SRHR and HIV/AIDS, Hafidha works to make mental health tools, wellness conversations and "
     "personal development resources more accessible to everyday communities.",
     None),

    ("Hon. Patrick Mbelle",
     "MCA, Bamburi Ward &#183; Founder &amp; Patron, The Mbelle Initiative",
     "Hon. Patrick Mbelle is the Member of County Assembly for Bamburi Ward and a community "
     "leader focused on youth development, skills-building and grassroots empowerment. He is the "
     "Founder and Patron of The Mbelle Initiative, as well as the Bamburi Skills Development "
     "Center, Mjini Shamba Community Enterprise, and Mentors of the Seas Centre. Through these "
     "initiatives, he supports young people and communities through practical skills development, "
     "enterprise, mentorship and locally driven opportunities for growth.",
     None),

    ("Gheida Abdala Omar",
     "Founder, Girls I Save Africa (GiSave) &#183; STEM Education Advocate &amp; Innovator",
     "Gheida Abdala Omar is a Kenyan STEM education advocate, innovator, and the Founder of Girls "
     "I Save Africa (GiSave), a youth-led organisation empowering young people, especially girls, "
     "through STEM education, digital skills and innovation. She is a recipient of the "
     "Presidential Innovation Award 2025, Young Scientists Kenya Winner 2021, the Innovation for "
     "Social Change Award, and the Pwani Women Golden Awards Rising Star 2023. In 2025, she was a "
     "Microsoft Imagine Cup Finalist and received the Global Internet Award at the World Internet "
     "Conference in China. In 2026, Gheida was recognised with the Women in STEM Award Kenya and "
     "completed the U.S. State Department-supported Community Engagement Exchange Program at "
     "Arizona State University. She also serves as an ITU Generation Connect Youth Envoy, Ban "
     "Ki-moon Foundation Scholar, Mastercard Foundation Alumni Committee Lead, and IFRC Global "
     "Innovation Lead. Her work is driven by a commitment to helping young people use technology, "
     "creativity and innovation to solve real community challenges and create meaningful impact.",
     None),

    ("Fiona Nuwamanya",
     "Finance &amp; Management Professional &#183; Entrepreneur &#183; Co-Founder, Africa Centre "
     "for Applied Digital Health",
     "Fiona Nuwamanya is a finance and management professional who believes that most great ideas "
     "do not fail for lack of ambition, but rather for lack of structure. Over the last 15+ "
     "years, she has founded TWAM Synergies, a consultancy firm supporting SMEs, co-founded "
     "Rocket Health, the first telemedicine company in Uganda, which scaled to over 1 million "
     "patients and raised a $5 million Series A, and was recognised as Africa’s SME CFO of the "
     "Year. She is now co-founder of the Africa Centre for Applied Digital Health (CADH), where "
     "she is helping drive AI-powered digital health solutions and research across the continent. "
     "Her mission is to help young founders build strong, sustainable businesses that last.",
     None),

    ("Kanga Rasi",
     "Director of Campaigns &amp; Advocacy, Brave Movement &#183; Advocate of the High Court of Kenya",
     "Kanga Rasi knew by age ten that she wanted to work protecting girls and women. She trained "
     "as a lawyer in Kenya believing the law alone could protect children, before learning that "
     "laws only change when people organise. That shift took her from courtrooms into campaigns "
     "and, eventually, into some of the world’s most influential policy spaces. She is the "
     "Director of Campaigns and Advocacy at Brave Movement, in partnership with Together for "
     "Girls. Her work has included briefing G20 sherpas and negotiators, contributing to G20 and "
     "G7 commitments on child online safety, and supporting a global coalition of more than 150 "
     "organisations. Kanga has participated in WHO and UN sessions across Geneva, Vienna and New "
     "York, as well as African Union negotiations in Addis Ababa. Closer to home, she has worked "
     "with provincial government officials in Kenya to help translate global commitments into "
     "practical priorities and budget lines. Her belief is simple and unwavering: those closest "
     "to the pain should be closest to the power. She is an Advocate of the High Court of Kenya.",
     None),

    ("Jackline Waweru Wanjiru",
     "Founder &amp; Team Lead, Leadership4Impact &#183; Youth Advocate",
     "Jackline Waweru Wanjiru is a youth advocate and changemaker with over a decade of "
     "experience in SRHR, gender equality, youth leadership and policy advocacy. She is the "
     "Founder and Team Lead of Leadership4Impact, a Kilifi-based organisation mentoring young "
     "leaders, and currently serves as Program Manager for the Student Education Fund at the "
     "Community Health Promotion Fund. Her work has included national and county-level youth "
     "advocacy through initiatives such as K-CAT, Y-ACT, Kenya Ni Mimi, and various Kilifi County "
     "technical working groups, where she has contributed to youth, gender, SRHR, HIV and "
     "anti-GBV policy development. Jackline is a YALI Cohort 11 alumna and was among the Top 12 "
     "finalists in Kenya’s Ms President political leadership reality show. Her work is driven by "
     "a commitment to creating spaces where young people can lead, thrive and shape the future.",
     None),

    ("Nancy Moraa Okemwa",
     "Communications Lead, Swahilipot Hub Foundation &#183; Strategic Communicator &amp; Storyteller",
     "Nancy Moraa Okemwa is a strategic communicator, storyteller and creative industry "
     "enthusiast working across communications, media, digital storytelling, community engagement "
     "and creative programming. As Communications Lead at Swahilipot Hub Foundation, she leads "
     "communications across youth-focused programmes and media platforms, using storytelling and "
     "creative expression to amplify voices and bring ideas to life. Nancy believes creativity is "
     "more than talent. It is a tool for expression, influence, enterprise and social change. "
     "Through her work, she supports young creatives to find their voice, understand their "
     "audiences, build meaningful brands and transform creative ideas into sustainable "
     "opportunities.",
     None),
]

# The two documented panels. "themes" distils the moderator's question set for
# each panellist into what the panel actually explored - the run sheet itself
# stays internal. Days 3-4 are not yet documented.
INUKA_PANELS = [
    {
        "day": "Day 1",
        "n": "Panel 01",
        "title": "Lead from Within",
        "blurb": "Exploring self-awareness, resilience, values and purpose-driven leadership.",
        "time": "11:40 &#8211; 12:45",
        "moderator": ("Melvine Tabitha Opondo", "CSA Africa alumna 2025, Software Engineering track"),
        "themes": [
            ("Aseef Akram",
             "Building trust across young people, employers and entrepreneurs; how to develop the "
             "mindset to create opportunity rather than wait for it; the failure that shaped how "
             "he leads today."),
            ("Fatuma Ali",
             "Beginning before you have the resources or the answers; how identity and personal "
             "values shape the kind of leader you become; staying grounded in your original "
             "purpose as recognition and pressure grow."),
            ("Haytam Isse Abdullahi",
             "What young people need to understand about themselves before they can lead others; "
             "leading without a title, from within your family, school and community; holding on "
             "to your values in environments that reward the opposite."),
        ],
        "closing": "In one sentence, what does &#8220;leading from within&#8221; mean to you, and "
                   "what is one action every young person in this room can take today to begin "
                   "that journey?",
    },
    {
        "day": "Day 2",
        "n": "Panel 02",
        "title": "Positioning Yourself for Opportunities",
        "blurb": "Recognising your own value, and learning how to put it in front of the right "
                 "people.",
        "time": "11:15 &#8211; 12:20",
        "moderator": ("Pheny Mwaisaka", "CSA Africa alumna 2025, Data Science track"),
        "themes": [
            ("Kauthar Mohamed",
             "Identifying your strengths and communicating them with confidence; what to do while "
             "still in school or university to position yourself for what comes after; pursuing "
             "an opportunity before you feel fully qualified."),
            ("Edwin Njuga",
             "What distinguishes the young people who successfully access opportunities; the "
             "practical steps to funding, mentorship and partnership; the mistakes young people "
             "and MSMEs make when applying, and what to do instead."),
            ("Abdulkadir Aweis (Dadir)",
             "Building a personal brand that reflects your skills, values and ambitions; building "
             "genuine networks without making every interaction transactional; using creativity, "
             "storytelling and collaboration to make your own opportunities."),
        ],
        "closing": "What is one thing every young person here can do within the next 30 days to "
                   "position themselves for a meaningful opportunity?",
    },
]
