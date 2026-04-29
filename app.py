import streamlit as st

# Custom Styling to match the Maroon / Gold Beeai Morrison Brand
st.set_page_config(page_title="Bee-Morris Compatibility", page_icon="🐝")

st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    .stRadio > label { font-size: 1.1rem; font-weight: bold; color: #FFD700; margin-top: 15px; }
    .stButton>button { 
        background-color: #800000; 
        color: white; 
        border-radius: 10px; 
        border: 2px solid #FFD700;
        width: 100%;
        height: 3em;
        font-size: 1.2rem;
    }
    .stSuccess, .stWarning, .stError { font-size: 1.3rem; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐝 The Bee-Morris Compatibility Quiz")
st.write("Do you have what it takes to vibe with the brand? Let's find out.")

# The Full 20-Question Logic Bank
questions = [
    {"q": "1. How do you feel about working out 3-4 times in a week?", 
     "options": ["I'm super cool with it", "That's something I may like", "I'm too lazy for that", "Not possible"], "correct": "I'm super cool with it"},
    
    {"q": "2. How often should an adult shave their armpits and local government areas?", 
     "options": ["Twice a week", "Twice a month", "Once a month", "I like it bush-bush"], "correct": "Twice a week"},
    
    {"q": "3. What is your take about onions in food?", 
     "options": ["I love onions", "I'm indifferent about it", "I don't like it, but I can tolerate it", "I would rather drag my jajaina through broken bottles than eat onions"], "correct": "I love onions"},
    
    {"q": "4. What is your snoring intensity during night sleep?", 
     "options": ["I don't snore", "I snore mildly", "If you tap me, I might stop", "I'm the leader of generator gang"], "correct": "I don't snore"},
    
    {"q": "5. Late night vibecoding sessions until 3 AM?", 
     "options": ["I'll be right there with snacks", "I'll sleep while you work", "Can't you do that during the day?", "That sounds like a nightmare"], "correct": "I'll be right there with snacks"},
    
    {"q": "6. Your preferred morning routine start time?", 
     "options": ["5:00 AM - 6:30 AM", "8:00 AM - 9:00 AM", "11:00 AM", "Whenever my ancestors wake me up"], "correct": "5:00 AM - 6:30 AM"},
    
    {"q": "7. How do you handle a system design problem?", 
     "options": ["Model the logic first", "Start coding immediately", "Ask a bot to do it", "Cry in a corner"], "correct": "Model the logic first"},
    
    {"q": "8. What's the ideal weekend vibe?", 
     "options": ["Productive but chilled", "Strictly partying", "Sleeping for 48 hours", "Family reunions only"], "correct": "Productive but chilled"},
    
    {"q": "9. Spicy food tolerance levels?", 
     "options": ["Nigerian Pepper Soup level", "Mild heat", "Basically just salt", "Water is too spicy for me"], "correct": "Nigerian Pepper Soup level"},
    
    {"q": "10. Views on 'AI taking over'?", 
     "options": ["We are the AI now", "It's a useful tool", "I'm slightly worried", "I want to live in the woods with no tech"], "correct": "We are the AI now"},
    
    {"q": "11. Cleanliness in the workspace?", 
     "options": ["Everything has its place", "Organized chaos", "I can't see the desk", "What is a desk?"], "correct": "Everything has its place"},
    
    {"q": "12. How do you feel about 'Soulful' vs 'AI-sounding' content?", 
     "options": ["Keep it raw and real", "Balanced", "I like the AI polish", "Doesn't matter as long as it sells"], "correct": "Keep it raw and real"},
    
    {"q": "13. Preferred movie genre?", 
     "options": ["Sci-Fi/Tech Thriller", "Romance", "Documentaries", "Horror"], "correct": "Sci-Fi/Tech Thriller"},
    
    {"q": "14. How much social battery do you have?", 
     "options": ["High - I love people", "Medium - Selectively social", "Low - I prefer code", "Zero - I am a ghost"], "correct": "High - I love people"},
    
    {"q": "15. Taking photos of every meal before eating?", 
     "options": ["Never. Eat it while it's hot.", "Occasionally", "Always for the 'Gram", "Only if it looks like art"], "correct": "Never. Eat it while it's hot."},
    
    {"q": "16. Opinion on USSD vs. Internet apps?", 
     "options": ["USSD is king for accessibility", "I prefer apps", "What is USSD?", "Internet only"], "correct": "USSD is king for accessibility"},
    
    {"q": "17. Your take on 'Debt'?", 
     "options": ["Avoid it at all costs", "Leverage it wisely", "It’s a way of life", "I don't track it"], "correct": "Avoid it at all costs"},
    
    {"q": "18. How often do you read books?", 
     "options": ["Constantly learning", "Once a month", "I watch the summary", "I haven't read since high school"], "correct": "Constantly learning"},
    
    {"q": "19. Punctuality for a date?", 
     "options": ["15 mins early", "Exactly on time", "10 mins late", "I'll text when I'm leaving"], "correct": "15 mins early"},
    
    {"q": "20. Dealing with stress?", 
     "options": ["Vibecode it out", "Workout", "Eat", "Vent to anyone who listens"], "correct": "Vibecode it out"}
]

responses = []

# Form structure to prevent constant reloading
with st.form("compatibility_form"):
    for i, item in enumerate(questions):
        res = st.radio(item["q"], item["options"], key=f"q_{i}")
        responses.append(res)
    
    submitted = st.form_submit_button("Calculate My Compatibility Score")

if submitted:
    score = sum(1 for r, q in zip(responses, questions) if r == q["correct"])
    percentage = (score / len(questions)) * 100

    st.markdown("---")
    st.header(f"Result: {percentage:.0f}% Compatible")

    if percentage >= 90:
        st.success("🏆 **THE CHOSEN ONE.** You're practically Beeai's mirror image. Get in here!")
    elif percentage >= 70:
        st.info("✨ **SOLID VIBES.** We’d get along great, just keep your LGA maintenance on schedule.")
    elif percentage >= 50:
        st.warning("🧐 **POTENTIAL.** You're okay, but the onion situation might be a dealbreaker.")
    elif percentage >= 30:
        st.error("📉 **GENERATOR GANG.** I can hear your snoring from here. It's a no from me.")
    else:
        st.error("💀 **TERMINATED.** We are from two different planets. Please return to the motherboard.")
