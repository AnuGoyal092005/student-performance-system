import streamlit as st
import streamlit.components.v1 as components


def mobile_toggle():
    components.html(
        """
        <style>
        /* Sirf Mobile */
        @media (max-width:768px){

            #toggleBtn{
                position:fixed;
                top:15px;
                left:15px;
                width:42px;
                height:42px;
                border-radius:50%;
                border:none;
                background:#2D1B69;
                color:white;
                font-size:22px;
                cursor:pointer;
                z-index:999999;
                box-shadow:0 2px 8px rgba(0,0,0,.3);
            }

        }
        </style>

        <button id="toggleBtn">☰</button>

        <script>

        const btn=document.getElementById("toggleBtn");

        btn.onclick=function(){

            const sidebar=document.querySelector('[data-testid="stSidebar"]');

            if(!sidebar) return;

            if(sidebar.getAttribute("aria-expanded")=="true"){

                const closeBtn=document.querySelector('[data-testid="stSidebarCollapseButton"]');

                if(closeBtn){
                    closeBtn.click();
                }

            }else{

                const openBtn=document.querySelector('[data-testid="collapsedControl"]');

                if(openBtn){
                    openBtn.click();
                }

            }

        }

        </script>
        """,
        height=0,
    )