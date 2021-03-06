import React, { FC } from 'react'

// style
import './style/error404.scss'

interface ErrorProps {
    code?: string | number
    title?: string
    description?: string
}

const Error: FC<ErrorProps> = ({ title, code, description }) => {
    return (
        <div className='error-container'>
            <div className='stars'>
                <div id='stars'></div>
                <div id='stars2'></div>
                <div id='stars3'></div>
            </div>
            <div className='lamp__wrap'>
                <div className='lamp'>
                    <div className='cable'></div>
                    <div className='cover title'>{code}</div>
                    <div className='in-cover'>
                        <div className='bulb'></div>
                    </div>
                    <div className='light'></div>
                </div>
            </div>
            <section className='error'>
                <div className='error__content'>
                    <div className='error__message message'>
                        <h1 className='message__title title'>{title}</h1>
                        <p className='message__text title_small'>
                            {description}
                        </p>
                    </div>
                    <div className='error__nav e-nav'>
                        <a href='/' className='e-nav__link' />
                    </div>
                </div>
            </section>
        </div>
    )
}

export default Error
