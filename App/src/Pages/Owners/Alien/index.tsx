import React, { FC } from 'react'

// style
import './style/alien.scss'

// ICONS
import { IconType } from '@react-icons/all-files'
import { FaInstagram } from '@react-icons/all-files/fa/FaInstagram'
import { FaTelegram } from '@react-icons/all-files/fa/FaTelegram'
import { FaWhatsapp } from '@react-icons/all-files/fa/FaWhatsapp'

const Alien = () => {
    return (
        <section className='owner-container'>
            <section className='thumbnail-container'>
                <div
                    className='owner-thumbnail'
                    style={{
                        backgroundImage:
                            'url(https://cdn.discordapp.com/attachments/818500925660069934/945410974511415336/Sprite-0004.jpg)',
                    }}
                ></div>
                <div className='owner-profile'>
                    <div className='profile-image'></div>
                </div>
            </section>
            <section className='owner-content'>
                <div className='content-container'>
                    <div className='owner-name title'>Alien</div>
                    <div className='owner-descriotion title_small'>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        Vero corporis labore nulla molestiae est, illum id porro
                        Vero corporis labore nulla molestiae est, illum id
                        incidunt aspernatur, vel
                    </div>
                </div>
                <div className='owner-social'>
                    <div className='open-sea'>
                        <OpenSeaBtn color='blue' name='My Open Sea' />
                    </div>
                    <div className='owner-social-wrapper'>
                        <SocialBtn
                            name='telegram'
                            color='#00ccff'
                            ICON={FaTelegram}
                        />
                        <SocialBtn
                            name='Whatsapp'
                            color='#23b32a'
                            ICON={FaWhatsapp}
                        />
                        <SocialBtn
                            name='instagram'
                            color='#DD2A7B'
                            ICON={FaInstagram}
                        />
                    </div>
                </div>
            </section>
        </section>
    )
}

export default Alien

interface OpenSeaBtnProps {
    name: string
    color: string
}

const OpenSeaBtn: FC<OpenSeaBtnProps> = ({ name, color }) => {
    return (
        <div className={`open-sea-btn title_small ${color}`}>
            <div className='hover'>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
            {name}
        </div>
    )
}

interface SocialBtnProps {
    ICON: IconType
    name: string
    color: string
}

const SocialBtn: FC<SocialBtnProps> = ({ ICON, name, color }) => {
    color
    return (
        <div className={`social-btn ${name}`}>
            <div className='icon'>
                <ICON size={20} fill={color} />
            </div>
            <div className='hover'>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    )
}