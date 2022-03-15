import React, { FC, useEffect, useRef, useState } from 'react'

// style
import './style/owner.scss'

// ICONS
import { IconType } from '@react-icons/all-files'
import { FaInstagram } from '@react-icons/all-files/fa/FaInstagram'
import { FaTwitter } from '@react-icons/all-files/fa/FaTwitter'
import { FaEthereum } from '@react-icons/all-files/fa/FaEthereum'

// comps
import NFTCard from 'components/NFTCard'

// router
import { useParams } from 'react-router-dom'

// state
import { useDispatch, useSelector } from 'react-redux'
import { RootState } from 'state'
import { GetOwner } from 'state/actions/collection'

const Owner: FC = () => {
    const LazyRef = useRef<HTMLDivElement>(null)
    const [isIntersecting, setisIntersecting] = useState(false)
    const { username } = useParams()

    const OwnerState = useSelector((s: RootState) => s.Owner)
    const dispatch = useDispatch()

    useEffect(() => {
        if (!username) return
        dispatch(GetOwner(username))
    }, [dispatch])

    useEffect(() => {
        if (LazyRef.current && !isIntersecting) {
            var observer = new IntersectionObserver(([entry]) => {
                if (entry && entry.isIntersecting) {
                    setisIntersecting(true)
                    observer.disconnect()
                }
            })

            observer.observe(LazyRef.current)
        }
        return () => {
            if (observer) observer.disconnect()
        }
    }, [LazyRef])

    if (!OwnerState) return <></>

    return (
        <section className='owner-container'>
            <section className='thumbnail-container'>
                <div
                    className='owner-thumbnail'
                    style={{
                        backgroundImage: `url(${OwnerState.banner})`,
                    }}
                ></div>
                <div className='owner-profile'>
                    <div
                        className='profile-image'
                        style={{
                            backgroundImage: `url(${OwnerState.picture})`,
                        }}
                    />
                </div>
            </section>
            <section className='owner-content'>
                <div className='content-container'>
                    <div className='owner-name title'>
                        {OwnerState.username}
                    </div>
                    <div className='owner-wallet'>
                        <div className='icon'>
                            <FaEthereum size={20} />
                        </div>
                        <div className='holder'>{OwnerState.wallet}</div>
                        {/* <div className='holder'>0x7ae0...ae9a</div> */}
                    </div>
                    <div className='owner-descriotion title_small'>
                        {OwnerState.description}
                    </div>
                </div>
                <div className='owner-social'>
                    <div className='open-sea'>
                        <OpenSeaBtn
                            color='blue'
                            name='My Open Sea'
                            onClick={() => open(OwnerState.opensea)}
                        />
                    </div>
                    <div className='owner-social-wrapper'>
                        {OwnerState.twitter && (
                            <SocialBtn
                                link={
                                    'https://twitter.com/' + OwnerState.twitter
                                }
                                name='twitter'
                                color='#1DA1F2'
                                ICON={FaTwitter}
                            />
                        )}
                        {OwnerState.instagram && (
                            <SocialBtn
                                link={
                                    'https://www.instagram.com/' +
                                    OwnerState.instagram
                                }
                                name='instagram'
                                color='#DD2A7B'
                                ICON={FaInstagram}
                            />
                        )}
                    </div>
                </div>
            </section>
            <section className='owner-collection'>
                <div
                    className={`collection-title title ${
                        isIntersecting ? 'shown' : ''
                    }`}
                    ref={LazyRef}
                >
                    <span>My Collections</span>
                </div>
                <div className='collections-wrapper'>
                    {OwnerState.assets.map((a, index) => (
                        <NFTCard {...a} key={index} />
                    ))}
                </div>
            </section>
        </section>
    )
}

export default Owner

interface OpenSeaBtnProps {
    name: string
    color: string
    onClick: () => void
}

const OpenSeaBtn: FC<OpenSeaBtnProps> = ({ name, color, onClick }) => {
    return (
        <div className={`open-sea-btn title_small ${color}`} onClick={onClick}>
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
    link: string
}

const SocialBtn: FC<SocialBtnProps> = ({ ICON, name, color, link }) => {
    color
    return (
        <a className={`social-btn ${name}`} href={link}>
            <div className='icon'>
                <ICON size={20} fill={color} />
            </div>
            <div className='hover'>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </a>
    )
}