import streamlit as st
import time
import random
import emoji

def pomodoro_timer():
    st.title('Pomodoro for Wifey 👩‍💻🕰️')
    st.image('avocado_clock.png', width = 500)
    # Initialize or get the session state variables
    if 'session_seconds' not in st.session_state:
        st.session_state.session_seconds = 1500  # default 25 minutes
    if 'break_seconds' not in st.session_state:
        st.session_state.break_seconds = 300  # default 5 minutes
    if 'timer_running' not in st.session_state:
        st.session_state.timer_running = False
    if 'timer_paused' not in st.session_state:
        st.session_state.timer_paused = False


    st.sidebar.title('Pomodoro Settings 🛎️')
    st.sidebar.write("Adjust the session and break lengths to customize your Pomodoro experience.")
    
    # Set default values for the session and break
    session_time = st.sidebar.number_input('Session time (minutes)', min_value=1, value=25)
    break_time = st.sidebar.number_input('Break time (minutes)', min_value=1, value=5)

    # Convert minutes to seconds only when not running or at initial setup
    if not st.session_state.timer_running and not st.session_state.timer_paused:
        st.session_state.session_seconds = session_time * 60
        st.session_state.break_seconds = break_time * 60

    # Move Start/Pause and Reset buttons to the sidebar
    if st.sidebar.button('Start/Pause ⏯️'):
        if st.session_state.timer_running:
            st.session_state.timer_paused = True
            st.session_state.timer_running = False
        else:
            st.session_state.timer_running = True
            st.session_state.timer_paused = False

    if st.sidebar.button('Reset ⌛'):
        st.session_state.session_seconds = session_time * 60
        st.session_state.break_seconds = break_time * 60
        st.session_state.timer_running = False
        st.session_state.timer_paused = False

    # Timer display setup
    timer_display = st.empty()
    mins, secs = divmod(st.session_state.session_seconds, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    timer_display.header(f"Session Time Remaining: {timer}")

    # Timer functionality
    if st.session_state.timer_running:
        while st.session_state.session_seconds > 0 and st.session_state.timer_running:
            time.sleep(1)
            st.session_state.session_seconds -= 1
            mins, secs = divmod(st.session_state.session_seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            timer_display.header(f"Session Time Remaining: {timer}")

        if st.session_state.session_seconds == 0:
            st.success('Session complete! Time for a break!')
            random_reminders = ['### Vo da danh rang chua? 🪥😁',
                                '### Vo da an sang chua? 🥯🥛🍳🥗',
                                '### Vo da tam chua? 🛀🧴🪒🫧',
                                '### Vo da uong thuoc chua? 💊💪🏻',
                                '### Vo co them kem khong? 🍦']
            st.markdown(random.choice(random_reminders))
            st.markdown('# Du vo chua lam gi thi chong van yeu vo :heart: :bouquet: :heart:')

            while st.session_state.break_seconds > 0 and st.session_state.timer_running:
                time.sleep(1)
                st.session_state.break_seconds -= 1
                mins, secs = divmod(st.session_state.break_seconds, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                timer_display.header(f"Break Time Remaining: {timer}")

            if st.session_state.break_seconds == 0:
                st.success('Break complete! Start a new Pomodoro?')
                st.session_state.timer_running = False
                st.session_state.timer_paused = False

if __name__ == '__main__':
    pomodoro_timer()
