"""
Generate a synthetic fake news dataset for training.
Run this script to create dataset/fake_news.csv
"""
import csv
import random
import os

random.seed(42)

# Templates for generating synthetic news
REAL_TITLES = [
    "Federal Reserve Announces Interest Rate Decision for {year}",
    "Scientists Discover New Species in {location}",
    "Global Climate Summit Reaches Historic Agreement",
    "New Study Reveals Health Benefits of {food}",
    "Technology Company Reports Strong Quarterly Earnings",
    "International Space Station Completes Milestone Mission",
    "Government Passes New Infrastructure Bill",
    "Medical Researchers Make Breakthrough in {disease} Treatment",
    "Olympic Committee Announces Host City for {year}",
    "United Nations Calls for Action on Humanitarian Crisis",
    "Local Community Raises Funds for Disaster Relief",
    "University Study Shows Impact of Education on Economic Growth",
    "Central Bank Updates Monetary Policy Framework",
    "National Parks Service Reports Record Visitor Numbers",
    "Healthcare Workers Honored for Pandemic Response",
    "Renewable Energy Production Reaches New Record",
    "International Trade Agreement Signed Between Major Economies",
    "Space Agency Successfully Launches New Satellite",
    "Research Team Publishes Findings on Ocean Conservation",
    "City Council Approves New Public Transportation Plan",
]

FAKE_TITLES = [
    "SHOCKING: Secret Government Program Exposed by Insider",
    "You Won't Believe What This Celebrity Said About {topic}",
    "BREAKING: Scientists Finally Admit {claim} Was a Hoax",
    "This One Trick Will Make You a Millionaire Overnight",
    "Government Officials Caught in Massive Cover-Up",
    "EXPOSED: The Truth They Don't Want You to Know About {topic}",
    "Celebrity Found Living Secret Double Life in {location}",
    "ALERT: New Law Will Take Away Your {right} Rights",
    "Doctors Stunned by This Simple Home Remedy That Cures Everything",
    "URGENT: Banks Are About to Collapse — Withdraw Your Money Now",
    "Secret Society Controls World Governments According to Leaked Documents",
    "This Viral Photo Proves Everything We Believed Was Wrong",
    "BREAKING: Famous Person Secretly Working for Foreign Government",
    "Scientists Baffled: Mystery Object Found That Defies All Known Physics",
    "SHOCKING TRUTH: Popular Food Product Contains Dangerous Chemicals",
    "Hidden Camera Reveals What Really Happens in {location}",
    "This Country Secretly Developed a Weather Control Machine",
    "ALERT: Social Media Platform Caught Spying on All Users",
    "Time Traveler From {year} Warns About Upcoming Disaster",
    "Ancient Artifact Discovered That Rewrites Human History Completely",
]

REAL_TEXT_TEMPLATES = [
    "In a press conference held today, officials announced that the new policy will take effect starting next month. The decision was made after months of careful deliberation and consultation with experts in the field. Analysts predict that this change will have significant positive impacts on the economy and public welfare. The announcement was well received by industry leaders and the general public alike. Several independent verification agencies have confirmed the authenticity and validity of the data presented during the conference. The policy aims to address long-standing issues that have been identified through comprehensive research and analysis conducted over the past several years.",
    "Researchers at a leading university have published their findings in a peer-reviewed journal, describing a significant advancement in the field of science. The study, which involved over a thousand participants across multiple countries, provides strong evidence supporting the hypothesis that has been debated for decades. The research team used rigorous methodology including randomized controlled trials and statistical analysis to arrive at their conclusions. Experts in the field have praised the study for its thoroughness and scientific rigor. The findings have been independently verified by two other research institutions.",
    "The international summit concluded today with world leaders signing a multilateral agreement focused on addressing critical global challenges. Delegates from more than fifty countries participated in the three-day event, which featured panel discussions, workshops, and bilateral meetings. The agreement outlines specific targets and timelines for implementation, along with accountability mechanisms. Environmental groups and human rights organizations have expressed cautious optimism about the commitments made during the summit. Follow-up meetings are scheduled for the coming months to track progress.",
    "According to the latest quarterly report filed with regulatory authorities, the company reported revenue growth of twelve percent compared to the same period last year. The strong performance was driven by increased demand in key markets and successful product launches. Management highlighted improvements in operational efficiency and customer satisfaction scores. Independent financial analysts have reviewed the numbers and confirm they are consistent with broader industry trends. The company also announced plans to expand its workforce and invest in new research and development initiatives.",
    "Local authorities have implemented a new community initiative aimed at improving public safety and social services in the region. The program, developed in collaboration with community leaders and academic experts, includes provisions for education, healthcare access, and economic development. Early results show promising trends in several key metrics. The initiative has received funding from both government sources and private foundations. Community members who participated in the pilot program have reported positive experiences and tangible improvements in their daily lives.",
    "The national weather service has issued updated forecasts based on the latest satellite data and atmospheric models. Meteorologists are closely monitoring developing weather patterns that could affect several regions in the coming week. Emergency preparedness agencies have been notified and are ready to activate response plans if necessary. The public is advised to stay informed through official channels and follow safety guidelines. Historical data analysis suggests that similar weather patterns have occurred periodically over the past century.",
    "Healthcare officials released new guidelines today based on the latest clinical research and epidemiological data. The recommendations were developed by a panel of medical experts representing various specialties and were reviewed by independent advisory committees. The guidelines address prevention, diagnosis, and treatment protocols for common health conditions. Medical professionals across the country are being briefed on the updates. Patient advocacy groups have been consulted during the development process to ensure the guidelines are practical and accessible.",
    "The education department released annual performance data showing steady improvements in student achievement across multiple grade levels and subject areas. The data covers standardized test scores, graduation rates, and college readiness indicators. Education policy experts attribute the gains to increased investment in teacher training, curriculum development, and technology integration in classrooms. The department also noted a narrowing of achievement gaps between different demographic groups. Superintendent meetings are planned to discuss strategies for maintaining this positive trajectory.",
]

FAKE_TEXT_TEMPLATES = [
    "URGENT! You absolutely WILL NOT BELIEVE what has been happening behind closed doors. Top secret sources who cannot be named have exclusively revealed to us that EVERYTHING you thought you knew is WRONG! This information is being actively suppressed by powerful forces who want to keep the truth hidden. Share this article with everyone you know before it gets taken down! Multiple anonymous insiders have confirmed that this is the biggest scandal in history and the mainstream media is refusing to cover it because they are all controlled by the same people!!!",
    "A shocking new discovery has left scientists completely speechless and unable to explain what they found. This goes against everything we have been taught in schools and universities. The establishment is trying desperately to discredit this finding because it threatens their entire worldview and the billions of dollars in funding they receive. Wake up people! The evidence is overwhelming but they don't want you to see it! Independent researchers who tried to investigate were silenced and their work was destroyed!!! This is NOT a drill!",
    "BREAKING NEWS that the mainstream media is desperately trying to hide from you! A brave whistleblower has come forward with unbelievable evidence that proves the entire system is rigged against ordinary people. The elites have been running a secret program for decades and nobody knew about it until now. This changes EVERYTHING. If you care about your future and your family's safety you need to read this immediately and take action before it's too late! They will try to delete this article so screenshot it and share everywhere!!!",
    "Doctors and medical professionals around the world are SHOCKED by this simple trick that Big Pharma doesn't want you to know about! For years they have been making billions by keeping people sick when the cure was right under our noses the entire time! This ancient remedy was used for centuries before modern medicine tried to suppress it. Thousands of people have already tried it and the results are MIRACULOUS. Don't let them fool you any longer! The truth is finally coming out despite their attempts to censor it!",
    "EXPOSED! We have obtained classified documents that prove beyond any doubt that the government has been lying to the public for years. These documents were leaked by a high-ranking insider who risked everything to get the truth out. The evidence is IRREFUTABLE and shows a pattern of deception that goes all the way to the top. Media outlets that are controlled by the same interests are predictably ignoring this bombshell story. But we won't be silenced! The people deserve to know what is really going on!!!",
    "An anonymous source with connections to intelligence agencies has revealed a terrifying plot that will affect millions of people. According to this insider, the plan has been in motion for years and is about to reach its final phase. The signs are all around us but most people are too distracted to notice. Banks, governments, and tech companies are all involved in this massive conspiracy. This is your FINAL WARNING — prepare yourself and your family immediately! Everything you own could be worthless by next month!!!",
    "ALERT ALERT ALERT! A leading expert who was fired for speaking the truth has finally decided to go public with what he knows. For twenty years he was at the center of a massive operation designed to control the population without their knowledge or consent. He has documentation, recordings, and physical evidence that proves everything he is claiming. The authorities have already tried to silence him once and he fears for his life. This story is being shared through underground channels because every major platform has banned it!!!",
    "What they told you about history is completely and utterly FALSE! New evidence uncovered at a secret archaeological site proves that an advanced civilization existed thousands of years before what conventional science tells us. The artifacts found at this location include technology that should not have existed for another millennium. Mainstream archaeologists who visited the site were sworn to secrecy but one of them broke the agreement to share the truth with the world. Universities are scrambling to cover this up because it would destroy their reputations!!!",
]

LOCATIONS = ["Amazon Rainforest", "Pacific Ocean", "Arctic Region", "Mountain Range", "Underground Cave", "Remote Island", "Desert Region", "Ancient Forest"]
FOODS = ["green tea", "dark chocolate", "blueberries", "turmeric", "fermented foods", "leafy greens", "olive oil", "nuts"]
DISEASES = ["cancer", "diabetes", "heart disease", "Alzheimer's", "autoimmune disorders"]
TOPICS = ["vaccines", "climate change", "elections", "technology", "food safety", "energy", "healthcare", "education"]
RIGHTS = ["privacy", "free speech", "property", "gun", "voting", "healthcare"]
YEARS = ["2025", "2026", "2027", "2028", "2030", "2035"]
CLAIMS = ["global warming", "evolution", "the moon landing", "vaccines", "quantum physics"]

def fill_template(template):
    result = template
    result = result.replace("{location}", random.choice(LOCATIONS))
    result = result.replace("{food}", random.choice(FOODS))
    result = result.replace("{disease}", random.choice(DISEASES))
    result = result.replace("{topic}", random.choice(TOPICS))
    result = result.replace("{right}", random.choice(RIGHTS))
    result = result.replace("{year}", random.choice(YEARS))
    result = result.replace("{claim}", random.choice(CLAIMS))
    return result

def generate_dataset(num_samples=2000):
    rows = []
    half = num_samples // 2

    # Generate real news (label=1)
    for _ in range(half):
        title = fill_template(random.choice(REAL_TITLES))
        text = fill_template(random.choice(REAL_TEXT_TEMPLATES))
        # Add some variation
        sentences = text.split(". ")
        random.shuffle(sentences)
        count = random.randint(min(4, len(sentences)), len(sentences))
        text = ". ".join(sentences[:count])
        rows.append({"title": title, "text": text, "label": 1})

    # Generate fake news (label=0)
    for _ in range(half):
        title = fill_template(random.choice(FAKE_TITLES))
        text = fill_template(random.choice(FAKE_TEXT_TEMPLATES))
        sentences = text.split(". ")
        random.shuffle(sentences)
        count = random.randint(min(4, len(sentences)), len(sentences))
        text = ". ".join(sentences[:count])
        rows.append({"title": title, "text": text, "label": 0})

    random.shuffle(rows)
    return rows

if __name__ == "__main__":
    os.makedirs("dataset", exist_ok=True)
    data = generate_dataset(2000)

    with open("dataset/fake_news.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "text", "label"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Generated {len(data)} samples -> dataset/fake_news.csv")
